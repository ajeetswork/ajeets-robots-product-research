"""Representative checks for intentionally bounded research views."""

from src.collection_jobs import open_question_triage, recent_quote_preview


class FakeClient:
    def list_recent_quotes_page(self, *, limit, cursor=None, sort="-received_at"):
        return {"items": [{"id": f"q-{i}"} for i in range(limit)], "next_cursor": "more"}

    def list_open_questions_page(self, *, limit, cursor=None):
        return {"items": [{"id": f"o-{i}"} for i in range(limit)], "next_cursor": "more"}


def test_recent_quote_preview_is_ten_rows():
    assert len(recent_quote_preview(FakeClient())) == 10


def test_open_question_triage_is_twenty_five_rows():
    assert len(open_question_triage(FakeClient())) == 25
