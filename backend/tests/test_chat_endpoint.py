from backend.app import create_app


def test_chat_endpoint_success():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/chat",
        json={"message": "Olá, estou com palpitação leve há 2 dias."},
    )
    payload = response.get_json()

    assert response.status_code == 200
    assert "disclaimer" in payload
    assert payload["source"] in {"fallback_local", "watson"}


def test_chat_endpoint_rejects_invalid_payload():
    app = create_app()
    client = app.test_client()

    response = client.post("/api/chat", json={"message": "   "})

    assert response.status_code == 400
    assert response.get_json()["error"] == "payload_invalido"
