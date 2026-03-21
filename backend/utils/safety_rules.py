from dataclasses import dataclass


DISCLAIMER = (
    "Aviso: este assistente tem finalidade educacional e de triagem inicial simulada. "
    "Ele nao realiza diagnostico, nao prescreve medicamentos e nao substitui avaliacao medica."
)

URGENCY_TERMS = {
    "dor intensa no peito",
    "forte dor no peito",
    "aperto no peito",
    "falta de ar severa",
    "muita falta de ar",
    "desmaio",
    "desmaiei",
    "dor irradiando para o braço",
    "dor no braco esquerdo",
    "dor no braço esquerdo",
    "suor frio",
}


@dataclass
class SafetyResult:
    reply: str
    urgency_detected: bool
    follow_up: str | None = None


def detect_urgency(message: str) -> bool:
    normalized = message.lower()
    return any(term in normalized for term in URGENCY_TERMS)


def contains_diagnostic_request(message: str) -> bool:
    normalized = message.lower()
    diagnostic_terms = [
        "isso e infarto",
        "isso é infarto",
        "qual o diagnostico",
        "qual o diagnóstico",
        "tenho doenca cardiaca",
        "tenho doença cardiaca",
    ]
    diagnosis_verbs = [
        "diagnostique",
        "diagnosticar",
        "diagnostico",
        "diagnóstico",
    ]
    direct_request = "diagnost" in normalized and any(
        marker in normalized for marker in ["pode", "poderia", "me", "agora", "?"]
    )
    return any(term in normalized for term in diagnostic_terms) or any(
        verb in normalized for verb in diagnosis_verbs
    ) or direct_request


def apply_safety_rules(user_message: str, assistant_reply: str) -> SafetyResult:
    if detect_urgency(user_message):
        return SafetyResult(
            reply=(
                "Os sinais descritos podem indicar uma situacao de urgencia. "
                "Procure atendimento medico imediatamente ou acione um servico de emergencia. "
                "Se estiver acompanhado, evite dirigir e leve suas informacoes de saude se possivel."
            ),
            urgency_detected=True,
            follow_up="Encerrar a simulacao e orientar busca imediata por atendimento.",
        )

    if contains_diagnostic_request(user_message):
        return SafetyResult(
            reply=(
                "Nao posso confirmar diagnosticos. Posso apenas oferecer orientacoes educativas "
                "sobre sintomas, sinais de alerta e quando buscar avaliacao profissional."
            ),
            urgency_detected=False,
            follow_up="Reforcar limite de uso educacional do assistente.",
        )

    return SafetyResult(reply=assistant_reply, urgency_detected=False)
