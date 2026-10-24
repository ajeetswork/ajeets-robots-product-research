import csv
from io import StringIO


def load_manifest_rows(conn, batch_id):
    rows = conn.execute(
        """
        SELECT parcel_id, dispatch_sequence, customer_name, zone_code, carrier_code
        FROM outbound_parcels
        WHERE batch_id = ?
        ORDER BY dispatch_sequence ASC, parcel_id ASC
        """,
        (batch_id,),
    ).fetchall()

    return [
        {
            "parcel_id": row["parcel_id"],
            "dispatch_sequence": row["dispatch_sequence"],
            "customer_name": row["customer_name"],
            "zone_code": row["zone_code"],
            "carrier_code": row["carrier_code"],
        }
        for row in rows
    ]


def render_manifest_csv(conn, batch_id):
    output = StringIO()
    writer = csv.DictWriter(
        output,
        fieldnames=["parcel_id", "dispatch_sequence", "customer_name", "zone_code", "carrier_code"],
    )
    writer.writeheader()
    writer.writerows(load_manifest_rows(conn, batch_id))
    return output.getvalue()
