from dataclasses import dataclass, field
from typing import Any


@dataclass
class ChatRequest:
    message: str
    conversation_id: str | None = None
    context: dict[str, Any] = field(default_factory=dict)


@dataclass
class ChatResponse:
    reply: str
    source: str
    urgency_detected: bool
    disclaimer: str
    conversation_id: str | None = None
    detected_intents: list[str] = field(default_factory=list)
    detected_entities: list[str] = field(default_factory=list)
    follow_up: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "reply": self.reply,
            "source": self.source,
            "urgency_detected": self.urgency_detected,
            "disclaimer": self.disclaimer,
            "conversation_id": self.conversation_id,
            "detected_intents": self.detected_intents,
            "detected_entities": self.detected_entities,
            "follow_up": self.follow_up,
        }
