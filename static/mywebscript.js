async function RunSentimentAnalysis() {
    const text = document.getElementById("textToAnalyze").value;
    const output = document.getElementById("system_response");
    const button = document.getElementById("analyzeButton");
    button.disabled = true;
    output.textContent = "Analyzing...";
    try {
        const response = await fetch(
            "emotionDetector?" + new URLSearchParams({textToAnalyze: text})
        );
        output.textContent = await response.text();
    } catch {
        output.textContent = "Unable to connect. Please try again later.";
    } finally {
        button.disabled = false;
    }
}
