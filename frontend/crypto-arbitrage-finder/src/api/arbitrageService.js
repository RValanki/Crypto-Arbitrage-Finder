// src/api/arbitrageService.js
const API_URL = "http://127.0.0.1:8000/detect_arbitrage/"; // Update this to match your Django API endpoint

export const fetchArbitrageOpportunities = async () => {
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({}), // Send an empty JSON object as the request body
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data; // The response contains the `data` key with the array of opportunities
  } catch (error) {
    console.error("Error fetching arbitrage opportunities:", error);
    return { data: [] }; // Return an empty array if an error occurs
  }
};
