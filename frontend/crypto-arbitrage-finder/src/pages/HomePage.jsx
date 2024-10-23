// src/pages/HomePage.jsx
import React from 'react';
import TopBar from '../components/TopBar'; // Adjust the import path as necessary
import Refresh from '../components/Refresh';
import ArbitragePair from '../components/ArbitragePair';

const HomePage = () => {
  return (
    <div>
      <TopBar /> {/* Add the TopBar component here */}

      <h1 className="w-full h-[10vh] text-white font-bold text-5xl ml-32 mt-32">
        Crypto Arbitrage Finder
      </h1>

      {/* Flexbox layout with two columns */}
      <div className="flex mt-10 ml-20 mr-20"> {/* Add margin-top for spacing */}
        {/* First Column (3/4 width) */}
        <div className="flex-[5] p-4">
          <h2 className="text-white">First Column</h2>

          <div className="w-full  bg-[#1F2025] rounded-[5px] p-2">
            {/* Content for the first column */}


            <ArbitragePair> </ArbitragePair>
            <ArbitragePair> </ArbitragePair>
            <ArbitragePair> </ArbitragePair>
            <ArbitragePair> </ArbitragePair>
            <ArbitragePair> </ArbitragePair>
            <ArbitragePair> </ArbitragePair>
            <ArbitragePair> </ArbitragePair>
            <ArbitragePair> </ArbitragePair>
            <ArbitragePair> </ArbitragePair>
            <ArbitragePair> </ArbitragePair>
            <ArbitragePair> </ArbitragePair>
            <ArbitragePair> </ArbitragePair>
            <ArbitragePair> </ArbitragePair>
            

          </div>
        </div>

        {/* Second Column (1/4 width) */}
        <div className="flex-[1.6] p-4 flex flex-col">
          

          {/* Three Rows in Second Column */}
          <div className=" h-[15vh] bg-[#1F2025] rounded-[5px] mt-6 mb-4 p-2">
            <Refresh> </Refresh>
          </div>
          <div className="h-[30vh] bg-[#1F2025] rounded-[5px] mb-4 p-2">
            
          </div>
          <div className=" h-[30vh] bg-[#1F2025] rounded-[5px] p-2">
            
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
