from logic.api_calls import get_todos, URL
import responses


@responses.activate
def test_get_todos():
    responses.add(
        responses.GET,
        URL,
        body='{"todos": [{"id": 1, "todo": "Todo 1"}, {"id": 2, "todo": "Todo 2"}]}',
        content_type="application/json"
    )
    response = get_todos()
    assert response == {
        "todos": [
            {"id": 1, "todo": "Todo 1"},
            {"id": 2, "todo": "Todo 2"}
        ]
    }
