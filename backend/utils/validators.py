from backend.models.message_models import ChatRequest


class ValidationError(ValueError):
    pass


def validate_chat_payload(payload: dict | None) -> ChatRequest:
    if payload is None:
        raise ValidationError("O corpo da requisição deve ser um JSON válido.")

    if "message" not in payload:
        raise ValidationError("O campo 'message' é obrigatório.")

    message = payload.get("message")
    if not isinstance(message, str):
        raise ValidationError("O campo 'message' deve ser uma string.")

    normalized = message.strip()
    if not normalized:
        raise ValidationError("Informe uma mensagem não vazia para continuar.")

    conversation_id = payload.get("conversation_id")
    if conversation_id is not None and not isinstance(conversation_id, str):
        raise ValidationError("O campo 'conversation_id' deve ser uma string.")

    context = payload.get("context") or {}
    if not isinstance(context, dict):
        raise ValidationError("O campo 'context' deve ser um objeto JSON.")

    return ChatRequest(
        message=normalized,
        conversation_id=conversation_id,
        context=context,
    )
