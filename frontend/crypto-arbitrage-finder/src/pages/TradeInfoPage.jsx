// src/pages/TradeInfoPage.jsx
import React from 'react';
import TopBar from '../components/TopBar';
import CryptoPriceCard from '../components/CryptoPriceCard';

const TradeInfoPage = () => {
  return (
    <div>
      <TopBar /> {/* Add the TopBar component here */}
      <div class="flex mt-24">
        <div class="flex justify-center w-1/2 h-[500px] ml-48 px-8">
          <CryptoPriceCard> </CryptoPriceCard>
        </div>

        <div class="flex justify-center w-1/2 h-[500px] mr-48 px-8">
          <CryptoPriceCard> </CryptoPriceCard>
        </div>

      </div>



    </div>
  );
};

export default TradeInfoPage;
