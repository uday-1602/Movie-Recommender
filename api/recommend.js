export default async function handler(req, res) {
    // Only allow POST requests
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method not allowed' });
    }

    // Grabs the user's query from the frontend
    const { search_query } = req.body;
    
    // Grabs the hidden AWS URL from Vercel's secure environment variables
    const AWS_API_URL = process.env.AWS_API_URL;

    try {
        // Securely calls the AWS API Gateway from the server
        const awsResponse = await fetch(`${AWS_API_URL}/recommend`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ search_query })
        });

        const data = await awsResponse.json();
        
        // Send the result back to the frontend
        return res.status(200).json(data);
        
    } catch (error) {
        console.error("Proxy error:", error);
        return res.status(500).json({ error: 'Failed to connect to AI' });
    }
}