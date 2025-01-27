chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === "classifyUrl") {
      fetch("http://127.0.0.1:5000/classify", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ url: message.url })
      })
        .then((response) => response.json())
        .then((data) => {
          sendResponse({ type: data.type });
        })
        .catch((error) => console.error("Error:", error));
  
      return true; // Keep the messaging channel open for sendResponse
    }
  });
  