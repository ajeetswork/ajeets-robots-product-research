def load_digest_items(conn, account_id):
    rows = conn.execute(
        """
        SELECT alert_id, priority_rank, created_at, title, summary
        FROM customer_alerts
        WHERE account_id = ? AND digest_ready = 1
        ORDER BY priority_rank ASC, created_at ASC, alert_id ASC
        """,
        (account_id,),
    ).fetchall()

    return [
        {
            "alert_id": row["alert_id"],
            "priority_rank": row["priority_rank"],
            "created_at": row["created_at"],
            "title": row["title"],
            "summary": row["summary"],
        }
        for row in rows
    ]


def build_digest_payload(conn, account_id):
    return {
        "account_id": account_id,
        "items": load_digest_items(conn, account_id),
    }
