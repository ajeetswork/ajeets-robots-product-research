from dataclasses import dataclass


@dataclass(frozen=True)
class WorkspaceContext:
    workspace_id: str
    actor_id: str
    roles: tuple[str, ...]


def require_workspace(request) -> WorkspaceContext:
    session = request.state.session
    if not session or not session.workspace_id:
        raise PermissionError("workspace session required")
    return WorkspaceContext(
        workspace_id=session.workspace_id,
        actor_id=session.user_id,
        roles=tuple(session.roles),
    )


def require_role(context: WorkspaceContext, allowed: set[str]) -> None:
    if not allowed.intersection(context.roles):
        raise PermissionError("role not permitted")
