import base64
import logging
import uuid
from typing import Any

import requests

from backend.config import Settings

LOGGER = logging.getLogger(__name__)


class WatsonService:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.sessions: dict[str, str] = {}

    def is_configured(self) -> bool:
        return self.settings.watson_enabled

    def get_reply(self, message: str, conversation_id: str | None = None) -> dict[str, Any]:
        if self.is_configured():
            try:
                return self._send_to_watson(message, conversation_id)
            except requests.RequestException as exc:
                LOGGER.warning("Falha ao consultar Watson Assistant: %s", exc)

        return self._local_fallback(message, conversation_id)

    def _send_to_watson(
        self, message: str, conversation_id: str | None = None
    ) -> dict[str, Any]:
        conversation_id = conversation_id or str(uuid.uuid4())
        session_id = self.sessions.get(conversation_id) or self._create_session()
        self.sessions[conversation_id] = session_id

        url = (
            f"{self.settings.watson_url}/v2/assistants/"
            f"{self.settings.watson_assistant_id}/sessions/{session_id}/message"
        )
        response = requests.post(
            url,
            headers={
                "Authorization": f"Basic {self._basic_token()}",
                "Content-Type": "application/json",
            },
            params={"version": self.settings.watson_assistant_version},
            json={"input": {"message_type": "text", "text": message}},
            timeout=15,
        )
        response.raise_for_status()
        payload = response.json()
        output = payload.get("output", {}).get("generic", [])
        texts = [item.get("text", "") for item in output if item.get("response_type") == "text"]

        return {
            "reply": " ".join(texts).strip() or self._local_fallback(message, conversation_id)["reply"],
            "source": "watson",
            "conversation_id": conversation_id,
            "detected_intents": [
                intent.get("intent") for intent in payload.get("output", {}).get("intents", [])
            ],
            "detected_entities": [
                entity.get("entity") for entity in payload.get("output", {}).get("entities", [])
            ],
            "follow_up": "Resposta gerada pelo IBM Watson Assistant.",
        }

    def _create_session(self) -> str:
        url = (
            f"{self.settings.watson_url}/v2/assistants/"
            f"{self.settings.watson_assistant_id}/sessions"
        )
        response = requests.post(
            url,
            headers={"Authorization": f"Basic {self._basic_token()}"},
            params={"version": self.settings.watson_assistant_version},
            timeout=15,
        )
        response.raise_for_status()
        return response.json()["session_id"]

    def _basic_token(self) -> str:
        token = f"apikey:{self.settings.watson_api_key}".encode("utf-8")
        return base64.b64encode(token).decode("utf-8")

    def _local_fallback(
        self, message: str, conversation_id: str | None = None
    ) -> dict[str, Any]:
        normalized = message.lower()
        conversation_id = conversation_id or str(uuid.uuid4())

        if any(term in normalized for term in ["oi", "ola", "olá", "bom dia", "boa tarde"]):
            reply = (
                "Olá. Sou o CardioIA, um assistente educacional de apoio a triagem inicial simulada. "
                "Descreva seu principal sintoma cardiológico e, se puder, informe duração e intensidade."
            )
            intents = ["saudacao"]
        elif any(term in normalized for term in ["dor no peito", "dor toracica", "dor torácica"]):
            reply = (
                "Dor no peito pode ter diferentes causas. Para uma orientação educativa inicial, "
                "observe há quanto tempo começou, se a dor é leve, moderada ou intensa e se existe "
                "falta de ar, tontura ou irradiação para braço e mandíbula."
            )
            intents = ["informar_dor_toracica"]
        elif any(term in normalized for term in ["falta de ar", "cansaco", "cansaço"]):
            reply = (
                "Falta de ar merece atenção ao contexto. Ela ocorre em repouso ou esforço? "
                "Se vier acompanhada de dor intensa no peito, desmaio ou piora rápida, a orientação segura "
                "é buscar atendimento imediatamente."
            )
            intents = ["informar_falta_de_ar"]
        elif any(term in normalized for term in ["palpitacao", "palpitação", "coração acelerado"]):
            reply = (
                "Palpitações podem ser percebidas como batimentos acelerados ou irregulares. "
                "Para fins educativos, vale observar frequência, duração, gatilhos e sintomas associados."
            )
            intents = ["informar_palpitacao"]
        elif any(term in normalized for term in ["eletro", "ecg", "ecocardiograma", "exame"]):
            reply = (
                "Posso oferecer uma explicação educacional geral sobre exames cardiovasculares, "
                "como ECG, ecocardiograma e teste ergométrico. Diga qual exame você quer entender."
            )
            intents = ["pedir_explicacao_exame"]
        elif any(term in normalized for term in ["tchau", "obrigado", "obrigada", "encerrar"]):
            reply = (
                "Encerrando a conversa com segurança. Se os sintomas persistirem, piorarem ou causarem "
                "preocupação, procure avaliação profissional."
            )
            intents = ["despedida"]
        else:
            reply = (
                "Posso ajudar com orientação educativa sobre sintomas cardiovasculares, sinais de alerta "
                "e exames comuns. Conte sua principal queixa, a duração e se houve piora recente."
            )
            intents = ["fallback"]

        entities = self._extract_entities(normalized)
        return {
            "reply": reply,
            "source": "fallback_local",
            "conversation_id": conversation_id,
            "detected_intents": intents,
            "detected_entities": entities,
            "follow_up": "Modo demonstracao offline ativado.",
        }

    def _extract_entities(self, normalized_message: str) -> list[str]:
        entities: list[str] = []
        if any(term in normalized_message for term in ["dor", "palpit", "tontura", "falta de ar"]):
            entities.append("sintoma")
        if any(term in normalized_message for term in ["dias", "semanas", "horas", "meses"]):
            entities.append("duracao")
        if any(term in normalized_message for term in ["leve", "moderada", "intensa", "forte"]):
            entities.append("intensidade")
        if any(term in normalized_message for term in ["ecg", "eletro", "ecocardiograma", "holter"]):
            entities.append("exame")
        return entities
