let loadingInterval; 

async function getRecommendation() {
    const outputDiv = document.getElementById('output');
    const query = document.getElementById('userInput').value;
    
    if(!query) return;

    const loadingPhrases = [
        "Scanning the archives...",
        "Consulting the movie critics...",
        "Grabbing some popcorn...",
        "Finalizing your recommendations..."
    ];
    let phraseIndex = 0;
    
    outputDiv.style.display = "block";
    outputDiv.innerHTML = `<div class="loading">${loadingPhrases[phraseIndex]}</div>`;
    
    loadingInterval = setInterval(() => {
        phraseIndex = (phraseIndex + 1) % loadingPhrases.length;
        outputDiv.innerHTML = `<div class="loading">${loadingPhrases[phraseIndex]}</div>`;
    }, 2000);

    try {
        //AWS API Gateway endpoint
        const response = await fetch('/api/recommend', {
            method: 'POST',
            body: JSON.stringify({ "search_query": query }),
            headers: { 'Content-Type': 'application/json' }
        });

        const data = await response.json();
        
        clearInterval(loadingInterval); 
        
        let rawText = data.recommendation || "No recommendation found.";
        
        // Converts Markdown bold to HTML bold
        let formattedText = rawText.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        // Converts line breaks to HTML breaks
        formattedText = formattedText.replace(/\n/g, '<br>');

        outputDiv.innerHTML = formattedText;
        
    } catch (error) {
        clearInterval(loadingInterval);
        outputDiv.innerText = "Error: Could not connect to the AI. Check console.";
        console.error(error);
    }
}