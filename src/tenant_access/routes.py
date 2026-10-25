from .context import require_role, require_workspace


def get_order_details(request, repo, order_id: str):
    context = require_workspace(request)
    require_role(context, {"ops_admin", "support"})
    order = repo.get_order_for_workspace(context.workspace_id, order_id)
    if not order:
        return {"status": 404}
    return {
        "status": 200,
        "body": {
            "id": order["id"],
            "customer_name": order["customer_name"],
            "status": order["status"],
            "total_cents": order["total_cents"],
        },
    }


def patch_order_status(request, repo, order_id: str):
    context = require_workspace(request)
    require_role(context, {"ops_admin"})
    payload = request.json()
    new_status = payload["status"]
    updated = repo.update_order_status(order_id, new_status)
    if not updated:
        return {"status": 404}
    return {"status": 204}


def list_shipments(request, repo):
    context = require_workspace(request)
    require_role(context, {"ops_admin", "support", "fulfillment"})
    status = request.query_params.get("status")
    shipments = repo.list_shipments_for_workspace(context.workspace_id, status)
    return {
        "status": 200,
        "body": [
            {
                "id": row["id"],
                "order_id": row["order_id"],
                "carrier": row["carrier"],
                "tracking_number": row["tracking_number"],
                "status": row["status"],
            }
            for row in shipments
        ],
    }


def get_robot_model(request, repo, model_id: str):
    context = require_workspace(request)
    require_role(context, {"ops_admin", "support", "fulfillment"})
    model = repo.get_robot_model_global(model_id)
    if not model:
        return {"status": 404}
    return {
        "status": 200,
        "body": {
            "id": model["id"],
            "sku": model["sku"],
            "display_name": model["display_name"],
            "generation": model["generation"],
            "service_class": model["service_class"],
        },
    }


def search_activity(request, repo):
    context = require_workspace(request)
    require_role(context, {"ops_admin"})
    actor_id = request.query_params.get("actor_id")
    requested_workspace = request.query_params.get("workspace_id", context.workspace_id)
    limit = min(int(request.query_params.get("limit", "50")), 200)
    rows = repo.list_activity_for_workspace(requested_workspace, actor_id, limit)
    return {
        "status": 200,
        "body": [
            {
                "id": row["id"],
                "actor_id": row["actor_id"],
                "action": row["action"],
                "object_type": row["object_type"],
                "object_id": row["object_id"],
                "created_at": row["created_at"],
            }
            for row in rows
        ],
    }
