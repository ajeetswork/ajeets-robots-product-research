from collections import Counter


def build_tag_count_snapshot(events):
    counts = Counter(
        tag
        for event in events
        for tag in event.get("tags", [])
    )

    return {
        "tag_counts": {
            tag: count
            for tag, count in counts.items()
        }
    }


def count_for_tag(snapshot, tag):
    return snapshot["tag_counts"].get(tag, 0)
