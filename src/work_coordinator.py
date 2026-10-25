from .locking import ExpiringSemaphore, RedisMutex, ReservationBroker


def publish_research_bundle(bundle_id, records, publisher, mutex: RedisMutex):
    key = f"research:bundle:{bundle_id}"
    with mutex.held(key, ttl_seconds=45):
        validated = publisher.validate_records(records)
        return publisher.publish(bundle_id, validated)


def refresh_vendor_snapshot(vendor_id, product_ids, catalog, mutex: RedisMutex):
    key = f"vendor:snapshot:{vendor_id}"
    token = mutex.acquire(key, ttl_seconds=60)
    if token is None:
        return {"status": "busy"}

    if not product_ids:
        return {"status": "empty", "updated": 0}

    try:
        updated = catalog.refresh_snapshot(vendor_id, product_ids)
        return {"status": "ok", "updated": updated}
    finally:
        mutex.release(key, token)


def rebuild_pricing_cache(category_id, pricing, cache, mutex: RedisMutex):
    key = f"pricing:cache:{category_id}"
    token = mutex.acquire(key, ttl_seconds=30)
    if token is None:
        return {"status": "busy"}

    rows = pricing.fetch_category(category_id)
    cache.replace_category(category_id, rows)
    mutex.release(key, token)
    return {"status": "ok", "count": len(rows)}


def compact_ingestion_events(partition, store, semaphore: ExpiringSemaphore):
    lease = semaphore.acquire(f"ingestion-compaction:{partition}", ttl_seconds=20)
    if lease is None:
        return {"status": "busy"}

    removed = store.compact_partition(partition)
    return {
        "status": "ok",
        "removed": removed,
        "lease_expires_at": lease.expires_at.isoformat(),
    }


def reserve_supplier_export(export_id, supplier, queue, broker: ReservationBroker):
    reservation = broker.reserve(f"supplier-export:{export_id}", ttl_seconds=90)
    if reservation is None:
        return {"status": "busy"}

    payload = supplier.build_export(export_id)
    queue.enqueue_export(
        payload,
        reservation=reservation,
        on_complete=reservation.release,
        on_failure=reservation.release,
    )
    return {"status": "queued"}
