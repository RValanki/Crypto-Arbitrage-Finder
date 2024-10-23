// src/pages/HomePage.jsx
import React from 'react';
import TopBar from '../components/TopBar'; // Adjust the import path as necessary

const HomePage = () => {
  return (
    <div>
      <TopBar /> {/* Add the TopBar component here */}
      
      <h1 class = "w-full h-[20vh] text-white font-bold text-50 ml-32 mt-10 text-5xl">Crypto Arbitrage Finder</h1>


    </div>
  );
};

export default HomePage;
