from backend.app import create_app
from backend.utils.safety_rules import apply_safety_rules, detect_urgency


def test_detect_urgency_by_keyword():
    assert detect_urgency("Estou com dor intensa no peito e suor frio.")


def test_apply_safety_rules_overrides_reply():
    result = apply_safety_rules(
        "Estou com falta de ar severa e desmaio.",
        "Resposta comum.",
    )

    assert result.urgency_detected is True
    assert "Procure atendimento medico imediatamente" in result.reply


def test_apply_safety_rules_blocks_diagnostic_request():
    result = apply_safety_rules(
        "Pode me diagnosticar agora?",
        "Resposta comum.",
    )

    assert result.urgency_detected is False
    assert "Nao posso confirmar diagnosticos" in result.reply


def test_chat_endpoint_urgency_scenario():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/chat",
        json={"message": "Estou com dor intensa no peito e dor no braço esquerdo."},
    )
    payload = response.get_json()

    assert response.status_code == 200
    assert payload["urgency_detected"] is True
