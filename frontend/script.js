const messagesEl = document.getElementById("messages");
const formEl = document.getElementById("chatForm");
const inputEl = document.getElementById("messageInput");
const sendButtonEl = document.getElementById("sendButton");
const clearButtonEl = document.getElementById("clearButton");
const statusBadgeEl = document.getElementById("statusBadge");
const statusDotEl = document.getElementById("statusDot");
const formErrorEl = document.getElementById("formError");
const promptGridEl = document.getElementById("promptGrid");

let conversationId = window.localStorage.getItem("cardioia_conversation_id") || null;
let loadingMessageEl = null;

function getTimeLabel() {
  return new Intl.DateTimeFormat("pt-BR", {
    hour: "2-digit",
    minute: "2-digit",
  }).format(new Date());
}

function buildMessageHeader(author) {
  const label = author === "user" ? "Você" : "CardioIA";
  return `<strong><span>${label}</span><small>${getTimeLabel()}</small></strong>`;
}

function appendMessage(author, text, options = {}) {
  const article = document.createElement("article");
  const variantClass = options.variant ? options.variant : "";
  article.className = `message ${author} ${options.alert ? "alert" : ""} ${variantClass}`.trim();
  article.innerHTML = `
    ${buildMessageHeader(author)}
    <div class="message__content">
      <div class="message__meta"></div>
      <span></span>
      <p class="message__note" hidden></p>
    </div>
  `;
  article.querySelector("span").textContent = text;
  const metaEl = article.querySelector(".message__meta");
  if (options.tag) {
    const tag = document.createElement("span");
    tag.className = `message-tag ${options.tagClass || "message-tag--neutral"}`;
    tag.textContent = options.tag;
    metaEl.appendChild(tag);
  }
  if (options.source) {
    const sourceTag = document.createElement("span");
    sourceTag.className = "message-tag message-tag--source";
    sourceTag.textContent = options.source;
    metaEl.appendChild(sourceTag);
  }
  if (!metaEl.children.length) {
    metaEl.remove();
  }
  const noteEl = article.querySelector(".message__note");
  if (options.note) {
    noteEl.hidden = false;
    noteEl.textContent = options.note;
  }
  messagesEl.appendChild(article);
  messagesEl.scrollTop = messagesEl.scrollHeight;
  return article;
}

function appendLoadingMessage() {
  loadingMessageEl = document.createElement("article");
  loadingMessageEl.className = "message assistant loading";
  loadingMessageEl.innerHTML = `
    ${buildMessageHeader("assistant")}
    <div class="typing-dots" aria-label="Assistente digitando">
      <span></span><span></span><span></span>
    </div>
  `;
  messagesEl.appendChild(loadingMessageEl);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function removeLoadingMessage() {
  if (loadingMessageEl) {
    loadingMessageEl.remove();
    loadingMessageEl = null;
  }
}

function setStatus(isLoading) {
  statusBadgeEl.textContent = isLoading ? "Analisando sua mensagem" : "Pronto para conversar";
  statusDotEl.parentElement.classList.toggle("is-loading", isLoading);
}

function setStatusMessage(text, mode = "default") {
  statusBadgeEl.textContent = text;
  statusDotEl.parentElement.classList.toggle("is-loading", mode === "loading");
}

function setLoadingState(isLoading) {
  sendButtonEl.disabled = isLoading;
  clearButtonEl.disabled = isLoading;
  inputEl.disabled = isLoading;
  setStatus(isLoading);
}

function showFormError(message) {
  formErrorEl.hidden = false;
  formErrorEl.textContent = message;
}

function hideFormError() {
  formErrorEl.hidden = true;
  formErrorEl.textContent = "";
}

async function sendMessage(message) {
  hideFormError();
  setLoadingState(true);
  appendMessage("user", message);
  appendLoadingMessage();

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message,
        conversation_id: conversationId,
      }),
    });

    const data = await response.json();
    removeLoadingMessage();

    if (!response.ok) {
      const errorMessage = data.message || "Não foi possível processar sua mensagem.";
      appendMessage("assistant", errorMessage, {
        alert: true,
        tag: "Erro de entrada",
        tagClass: "message-tag--warning",
      });
      showFormError(errorMessage);
      setStatusMessage("Erro ao processar", "default");
      return;
    }

    conversationId = data.conversation_id || conversationId;
    if (conversationId) {
      window.localStorage.setItem("cardioia_conversation_id", conversationId);
    }

    const isDiagnosticLimit = data.follow_up === "Reforcar limite de uso educacional do assistente.";
    const note = data.urgency_detected
      ? "Se houver agravamento, não continue na interface: procure atendimento imediatamente."
      : isDiagnosticLimit
        ? "O CardioIA pode orientar sobre sinais de alerta e próximos passos seguros, mas não confirmar diagnósticos."
        : "Lembrete: esta orientação é educativa e não substitui avaliação clínica.";

    const sourceLabel = data.source === "watson_assistant"
      ? "Watson Assistant"
      : data.source === "safety_override"
        ? "Regra de segurança"
        : "Fallback local";

    appendMessage("assistant", data.reply, {
      alert: data.urgency_detected,
      variant: isDiagnosticLimit ? "limit" : "",
      tag: data.urgency_detected
        ? "Atenção imediata"
        : isDiagnosticLimit
          ? "Limite do assistente"
          : "Orientação educacional",
      tagClass: data.urgency_detected
        ? "message-tag--warning"
        : isDiagnosticLimit
          ? "message-tag--limit"
          : "message-tag--neutral",
      note,
      source: sourceLabel,
    });
    setStatusMessage(
      data.urgency_detected
        ? "Alerta de urgência identificado"
        : isDiagnosticLimit
          ? "Limite de escopo aplicado"
          : "Resposta educacional entregue — " + sourceLabel,
      "default"
    );
  } catch (error) {
    removeLoadingMessage();
    const fallbackMessage =
      "Falha de comunicação com o backend. Verifique se a aplicação Flask está em execução.";
    appendMessage("assistant", fallbackMessage, {
      alert: true,
      tag: "Erro de conexão",
      tagClass: "message-tag--warning",
    });
    showFormError(fallbackMessage);
    setStatusMessage("Falha de conexão", "default");
  } finally {
    setLoadingState(false);
    inputEl.focus();
  }
}

formEl.addEventListener("submit", async (event) => {
  event.preventDefault();
  const message = inputEl.value.trim();

  if (!message) {
    showFormError("Informe uma mensagem antes de enviar.");
    inputEl.focus();
    return;
  }

  inputEl.value = "";
  await sendMessage(message);
});

inputEl.addEventListener("input", () => {
  inputEl.style.height = "auto";
  inputEl.style.height = `${Math.min(inputEl.scrollHeight, 240)}px`;
  if (!formErrorEl.hidden) {
    hideFormError();
  }
});

inputEl.addEventListener("keydown", async (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    formEl.requestSubmit();
  }
});

clearButtonEl.addEventListener("click", () => {
  messagesEl.innerHTML = "";
  conversationId = null;
  window.localStorage.removeItem("cardioia_conversation_id");
  hideFormError();
  renderWelcomeMessage();
  setStatusMessage("Conversa reiniciada", "default");
  inputEl.focus();
});

promptGridEl.addEventListener("click", (event) => {
  const button = event.target.closest(".prompt-chip");
  if (!button) {
    return;
  }

  inputEl.value = button.dataset.prompt || "";
  inputEl.focus();
});

function renderWelcomeMessage() {
  appendMessage(
    "assistant",
    "Olá. Sou o CardioIA, um assistente acadêmico de apoio educacional. Conte seu principal sintoma cardiovascular e, se puder, informe duração, intensidade e sintomas associados.",
    {
      tag: "Orientação educacional",
      tagClass: "message-tag--neutral",
      note: "Você pode começar por sintomas, sinais de alerta ou dúvidas sobre exames cardiovasculares.",
    }
  );
}

renderWelcomeMessage();
