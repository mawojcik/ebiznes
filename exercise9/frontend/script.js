let chatHistory = [];

document.getElementById("send-btn").addEventListener("click", async () => {
  const inputEl = document.getElementById("prompt-input");
  const userInput = inputEl.value.trim();
  if (!userInput) return;

  chatHistory.push({ role: "user", parts: [{ text: userInput }] });
  inputEl.value = "";
  updateChatUI();

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ history: chatHistory })
    });

    const data = await response.json();
    chatHistory.push({ role: "model", parts: [{ text: data.response }] });
    updateChatUI();
  } catch (err) {
    chatHistory.push({ role: "model", parts: [{ text: "Błąd połączenia z serwerem." }] });
    updateChatUI();
  }
});

function updateChatUI() {
  const box = document.getElementById("chat-box");
  box.innerHTML = "";
  chatHistory.forEach(msg => {
    const div = document.createElement("div");
    div.className = msg.role;
    div.textContent = `${msg.role === "user" ? "Ty" : "Asystent"}: ${msg.parts[0].text}`;
    box.appendChild(div);
  });
  box.scrollTop = box.scrollHeight;
}
