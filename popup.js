document.getElementById("classify").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      const url = tabs[0].url;
  
      chrome.runtime.sendMessage({ type: "classifyUrl", url: url }, (response) => {
        const result = document.getElementById("result");
        result.textContent = `The URL is classified as: ${response.type}`;
      });
    });
  });
  