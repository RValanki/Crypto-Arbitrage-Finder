const API_URL = "http://127.0.0.1:8000/detect_arbitrage/"; // Update this to match your Django API endpoint

// Function to call the /detect_arbitrage endpoint
export const fetchArbitrageOpportunities = async () => {
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({}), // Send an empty JSON object as the request body
    });

    // Check if the response is OK
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response body as JSON
    const data = await response.json();

    // Call fetch_all_arbitrage_opportunities function with the data
    fetch_all_arbitrage_opportunities(data);
  } catch (error) {
    console.error("Error fetching arbitrage opportunities:", error);
  }
};

// Function to process and log the fetched arbitrage opportunities
export const fetch_all_arbitrage_opportunities = (data) => {
  console.log("Fetched arbitrage opportunities:", data);
};
