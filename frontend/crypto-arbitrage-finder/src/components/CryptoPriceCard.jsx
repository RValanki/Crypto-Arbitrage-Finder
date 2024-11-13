// CryptoPriceCard.jsx

import React from 'react';
import Bitcoin from "../assets/Bitcoin.png";
import Coinbase from "../assets/Coinbase.png";
import GreenArrowUp from "../assets/GreenArrowUp.png";
import ExchangeInfoCard from './ExchangeInfoCard';

const CryptoPriceCard = () => {
    return (
        <div className="w-full h-full max-w-[750px]">
            <div className="flex justify-center text-2xl font-bold text-[#C2C2C2] mb-4">Exchange 1</div>

            <div className="w-full h-3/5 bg-[#1F2025] rounded-[5px] p-2 mb-4 md:min-w-[430px] ">
                <div className="w-full h-full bg-[#2B2F38] rounded-[5px] p-4 flex flex-col justify-between">

                    <div className="flex justify-between items-start h-full">
                        {/* Left Item */}
                        <div className="flex items-center">
                            <img src={Bitcoin} alt="Logo" className="h-16 ml-1 mr-2" />
                            <div className="flex flex-col">
                                <div className="text-white font-bold">Bitcoin</div>
                                <div className="text-[#B4B4B4] text-xs">BTC/USD</div>
                            </div>
                        </div>

                        {/* Center Item */}
                        <div className="flex items-center justify-center h-full mt-4">
                            <img src={GreenArrowUp} alt="Arrow Up" className="h-8 mr-2" />
                            <div className="text-white font-bold text-3xl mr-[1vw]">
                                $68,203.69
                            </div>
                        </div>

                        {/* Right Item */}
                        <div className="flex items-center mr-2">
                            <img src={Coinbase} alt="Logo" className="h-12 ml-1 mr-2" />
                            <div className="flex flex-col">
                                <div className="text-white font-semibold mr-8">Coinbase</div>
                            </div>
                        </div>
                    </div>

                    {/* Bottom Section for "hi" divs */}
                    <div className="flex justify-center w-full mb-2">
                        <div className="flex space-x-4 w-full">
                            <div class="bg-[#202229] rounded-[5px] w-1/4 flex flex-col justify-center items-center">
                                <div class="text-[#B4B4B4] text-sm mt-2">Market Cap</div>
                                <div class="text-white font-semibold mb-2">$72.78B</div>
                            </div>

                            <div class="bg-[#202229] rounded-[5px] w-1/4 flex flex-col justify-center items-center">
                                <div class="text-[#B4B4B4] text-sm mt-2">Volume</div>
                                <div class="text-white font-semibold mb-2">$72.78B</div>
                            </div>

                            <div class="bg-[#202229] rounded-[5px] w-1/4 flex flex-col justify-center items-center">
                                <div class="text-[#B4B4B4] text-sm mt-2">High</div>
                                <div class="text-white font-semibold mb-2">$72.78B</div>
                            </div>

                            <div class="bg-[#202229] rounded-[5px] w-1/4 flex flex-col justify-center items-center">
                                <div class="text-[#B4B4B4] text-sm mt-2">Low</div>
                                <div class="text-white font-semibold mb-2">$72.78B</div>
                            </div>

                        </div>
                    </div>

                </div>
            </div>

            <ExchangeInfoCard> </ExchangeInfoCard>
        </div>
    );
};

export default CryptoPriceCard;
