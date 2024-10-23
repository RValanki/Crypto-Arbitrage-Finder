// src/components/AboutComponent.jsx
import React from 'react';
import FilterComponent from './FilterComponent';

const AboutComponent = () => {
  return (
    <div class = "w-full h-full">
        <div class = "ml-4 mt-2 text-white font-bold">
            About
        </div>
        <div class = "mx-4 mt-2 text-white text-xs">
        Crypto arbitrage, specifically in the context of cross-exchange arbitrage, refers to the practice of exploiting price discrepancies for the same cryptocurrency across different trading platforms. Traders buy a cryptocurrency on one exchange where the price is lower and simultaneously sell it on another exchange where the price is higher. This strategy takes advantage of the inefficiencies in the market, allowing traders to secure profits from the differences in pricing. Due to the fast-paced nature of cryptocurrency markets, successful arbitrage often relies on quick execution and access to multiple exchanges, making it an attractive yet competitive approach for traders seeking to capitalize on market fluctuations.
        </div>
        
        
    </div>
  );
};

export default AboutComponent;
