async function sendPrompt() {
  const prompt = document.getElementById("prompt").value;
  const responseBox = document.getElementById("response");
  responseBox.textContent = "Czekaj...";

  try {
    console.log("Wysyłam zapytanie:", prompt);
    const res = await fetch("http://127.0.0.1:5000/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt })
    });

    console.log("Status odpowiedzi:", res.status);
    if (!res.ok) {
      responseBox.textContent = `Błąd serwera: ${res.status} ${res.statusText}`;
      return;
    }

    const data = await res.json();
    console.log("Odpowiedź z backendu:", data);

    if (data.response) {
      responseBox.textContent = data.response;
    } else {
      responseBox.textContent = "Brak odpowiedzi.";
    }
  } catch (err) {
    responseBox.textContent = "Błąd połączenia: " + err.message;
    console.error(err);
  }
}
