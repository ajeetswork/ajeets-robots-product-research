"""Collection API client primitives used by Ajeet's Robots data workflows."""

from typing import Any, Callable


class ProductResearchApiClient:
    def get(self, path: str, *, params: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError

    def list_supplier_candidates_page(self, *, status: str, limit: int = 50, cursor: str | None = None):
        return self.get("/v1/supplier-candidates", params={"status": status, "limit": limit, "cursor": cursor})

    def list_research_sources_page(self, *, active_only: bool, limit: int = 100, cursor: str | None = None):
        return self.get("/v1/research-sources", params={"active_only": active_only, "limit": limit, "cursor": cursor})

    def list_recent_quotes_page(self, *, limit: int = 10, cursor: str | None = None, sort: str = "-received_at"):
        return self.get("/v1/quotes", params={"limit": limit, "cursor": cursor, "sort": sort})

    def list_price_observations_page(self, *, review_date: str, limit: int = 100, cursor: str | None = None):
        return self.get("/v1/price-observations", params={"review_date": review_date, "limit": limit, "cursor": cursor})

    def list_open_questions_page(self, *, limit: int = 25, cursor: str | None = None):
        return self.get("/v1/open-questions", params={"limit": limit, "cursor": cursor})


def collect_all(fetch_page: Callable[..., dict[str, Any]], **kwargs: Any) -> list[dict[str, Any]]:
    """Traverse a cursor-paginated collection until no continuation cursor remains."""
    items: list[dict[str, Any]] = []
    cursor: str | None = None

    while True:
        page = fetch_page(cursor=cursor, **kwargs)
        items.extend(page.get("items", []))
        cursor = page.get("next_cursor")
        if not cursor:
            return items
