// src/pages/TradeInfoPage.jsx
import React from 'react';
import TopBar from '../components/TopBar';
import CryptoPriceCard from '../components/CryptoPriceCard';
import TradeLegComponent from '../components/TradeLegComponent';
import TotalProfitComponent from '../components/TotalProfitComponent';

const TradeInfoPage = () => {
  return (
    <div>
     {/* Add the TopBar component here */}
     <TopBar />
      <div className="animate-fadeInFast">
        <div className="flex flex-col md-lg:flex-row mt-28">
          <div className="flex justify-center w-full md-lg:w-1/2 h-[500px] md-lg:px-8 sm:px-24 px-4 mb-4 md-lg:mb-0 md-lg:ml-48 ml-0"> {/* Reduced padding */}
            <CryptoPriceCard />
          </div>

          <div className="flex justify-center w-full md-lg:w-1/2 h-[500px] md-lg:px-8 sm:px-24 px-4 md-lg:mr-48 mr-0"> {/* Reduced padding */}
            <CryptoPriceCard />
          </div>
        </div>

        {/* Centering the div with "hi" */}
        <div className="flex justify-center mt-12">
          <div className="md-lg:w-3/5 sm:w-4/5 w-full">
            <div className="mb-8">
              <TradeLegComponent />
            </div>

            <div className="mb-16">
              <TradeLegComponent isBuy={false}/>
            </div>

            
          </div>
        </div>

        <div className="flex justify-center">

        <div className="mb-24">
              <TotalProfitComponent />
            </div>
        </div>
      </div>
    </div>
  );
};

export default TradeInfoPage;
