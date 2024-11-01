// src/pages/TradeInfoPage.jsx
import React from 'react';
import TopBar from '../components/TopBar';
import CryptoPriceCard from '../components/CryptoPriceCard';
import ExchangeInfoCard from '../components/ExchangeInfoCard';
import TradeLegComponent from '../components/TradeLegComponent';
import TotalProfitComponent from '../components/TotalProfitComponent';

const TradeInfoPage = () => {
  return (
    <div>
      <TopBar /> {/* Add the TopBar component here */}
      <div class = "animate-fadeInFast">
      <div className="flex mt-28">
        <div className="flex justify-center w-1/2 h-[500px] ml-48 px-8">
          <CryptoPriceCard />
        </div>

        <div className="flex justify-center w-1/2 h-[500px] mr-48 px-8">
          <CryptoPriceCard />
        </div>
      </div>

      {/* Centering the div with "hi" */}
      <div className="flex justify-center mt-12">
        <div className="w-3/5">
          <div class = "mb-8">
            <TradeLegComponent> </TradeLegComponent>
          </div>
          
          <div class = "mb-16">
            <TradeLegComponent> </TradeLegComponent>
          </div>

          <div class = "mb-24">
            <TotalProfitComponent> </TotalProfitComponent>
          </div>
        </div>

       
      </div>
      </div>
    </div>
  );
};

export default TradeInfoPage;
