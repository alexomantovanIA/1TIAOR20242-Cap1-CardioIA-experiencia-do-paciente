from flask import Blueprint, request, jsonify

from backend.services.watson_service import WatsonService
from backend.utils.validators import validate_message, sanitize_message

chat_bp = Blueprint("chat", __name__)

watson_service = WatsonService()


@chat_bp.route("/api/chat", methods=["POST"])
def chat():
    body = request.get_json(silent=True)

    if not body or "message" not in body:
        return jsonify({"message": "Campo 'message' e obrigatorio no corpo da requisicao."}), 400

    raw_message = body.get("message", "")
    conversation_id = body.get("conversation_id")

    is_valid, error_msg = validate_message(raw_message)
    if not is_valid:
        return jsonify({"message": error_msg}), 400

    message = sanitize_message(raw_message)
    response = watson_service.send_message(message, conversation_id)

    return jsonify(response.to_dict()), 200


@chat_bp.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "watson_connected": watson_service.is_connected,
        "mode": "watson_assistant" if watson_service.is_connected else "fallback_local",
    }), 200
