def load_pick_wave_routes(conn, wave_id):
    rows = conn.execute(
        """
        SELECT route_id, route_sequence, station_code, tote_count
        FROM pick_wave_routes
        WHERE wave_id = ?
        """,
        (wave_id,),
    ).fetchall()

    route_by_id = {
        row["route_id"]: {
            "route_id": row["route_id"],
            "route_sequence": row["route_sequence"],
            "station_code": row["station_code"],
            "tote_count": row["tote_count"],
        }
        for row in rows
    }

    return list(route_by_id.values())


def build_pick_wave_export(conn, wave_id):
    return {
        "wave_id": wave_id,
        "routes": load_pick_wave_routes(conn, wave_id),
    }
