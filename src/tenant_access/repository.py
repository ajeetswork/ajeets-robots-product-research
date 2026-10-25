class OperationsRepository:
    def __init__(self, db):
        self.db = db

    def get_order(self, order_id: str):
        return self.db.fetch_one(
            "SELECT id, workspace_id, customer_name, status, total_cents "
            "FROM orders WHERE id = :order_id",
            {"order_id": order_id},
        )

    def get_order_for_workspace(self, workspace_id: str, order_id: str):
        return self.db.fetch_one(
            "SELECT id, workspace_id, customer_name, status, total_cents "
            "FROM orders WHERE workspace_id = :workspace_id AND id = :order_id",
            {"workspace_id": workspace_id, "order_id": order_id},
        )

    def update_order_status(self, order_id: str, status: str):
        return self.db.execute(
            "UPDATE orders SET status = :status, updated_at = CURRENT_TIMESTAMP "
            "WHERE id = :order_id",
            {"order_id": order_id, "status": status},
        )

    def update_order_status_for_workspace(
        self, workspace_id: str, order_id: str, status: str
    ):
        return self.db.execute(
            "UPDATE orders SET status = :status, updated_at = CURRENT_TIMESTAMP "
            "WHERE workspace_id = :workspace_id AND id = :order_id",
            {"workspace_id": workspace_id, "order_id": order_id, "status": status},
        )

    def list_shipments_for_workspace(self, workspace_id: str, status: str | None):
        sql = (
            "SELECT id, order_id, carrier, tracking_number, status, created_at "
            "FROM shipments WHERE workspace_id = :workspace_id"
        )
        params = {"workspace_id": workspace_id}
        if status:
            sql += " AND status = :status"
            params["status"] = status
        sql += " ORDER BY created_at DESC"
        return self.db.fetch_all(sql, params)

    def get_robot_model_global(self, model_id: str):
        return self.db.fetch_one(
            "SELECT id, sku, display_name, generation, service_class "
            "FROM robot_models WHERE id = :model_id",
            {"model_id": model_id},
        )

    def list_activity_for_workspace(
        self, workspace_id: str, actor_id: str | None, limit: int
    ):
        sql = (
            "SELECT id, workspace_id, actor_id, action, object_type, object_id, created_at "
            "FROM activity_log WHERE workspace_id = :workspace_id"
        )
        params = {"workspace_id": workspace_id, "limit": limit}
        if actor_id:
            sql += " AND actor_id = :actor_id"
            params["actor_id"] = actor_id
        sql += " ORDER BY created_at DESC LIMIT :limit"
        return self.db.fetch_all(sql, params)
