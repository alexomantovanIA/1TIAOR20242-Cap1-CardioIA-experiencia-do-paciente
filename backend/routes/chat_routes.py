from flask import Blueprint, current_app, jsonify, request

from backend.models.message_models import ChatResponse
from backend.utils.safety_rules import DISCLAIMER, apply_safety_rules
from backend.utils.validators import ValidationError, validate_chat_payload

chat_bp = Blueprint("chat", __name__)


@chat_bp.get("/health")
def healthcheck():
    return jsonify({"status": "ok", "service": "CardioIA Fase 5"})


@chat_bp.post("/api/chat")
def chat():
    try:
        chat_request = validate_chat_payload(request.get_json(silent=True))
    except ValidationError as exc:
        return (
            jsonify(
                {
                    "error": "payload_invalido",
                    "message": str(exc),
                }
            ),
            400,
        )

    service_response = current_app.config["WATSON_SERVICE"].get_reply(
        chat_request.message, chat_request.conversation_id
    )
    safety_result = apply_safety_rules(chat_request.message, service_response["reply"])

    response = ChatResponse(
        reply=safety_result.reply,
        source=service_response["source"],
        urgency_detected=safety_result.urgency_detected,
        disclaimer=DISCLAIMER,
        conversation_id=service_response.get("conversation_id"),
        detected_intents=service_response.get("detected_intents", []),
        detected_entities=service_response.get("detected_entities", []),
        follow_up=safety_result.follow_up or service_response.get("follow_up"),
    )
    return jsonify(response.to_dict())
