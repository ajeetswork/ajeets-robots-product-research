"""Collection readers used by supplier and market-research workflows."""

from .collection_api import ProductResearchApiClient, collect_all


def export_approved_supplier_candidates(client: ProductResearchApiClient) -> list[dict]:
    page = client.list_supplier_candidates_page(status="approved", limit=50)
    return page.get("items", [])


def sync_active_research_sources(client: ProductResearchApiClient) -> list[dict]:
    return collect_all(
        client.list_research_sources_page,
        active_only=True,
        limit=100,
    )


def recent_quote_preview(client: ProductResearchApiClient) -> list[dict]:
    page = client.list_recent_quotes_page(limit=10, sort="-received_at")
    return page.get("items", [])


def build_price_review_index(client: ProductResearchApiClient, review_date: str) -> dict[str, dict]:
    page = client.list_price_observations_page(review_date=review_date, limit=100)
    return {row["sku"]: row for row in page.get("items", [])}


def open_question_triage(client: ProductResearchApiClient) -> list[dict]:
    page = client.list_open_questions_page(limit=25)
    return page.get("items", [])
