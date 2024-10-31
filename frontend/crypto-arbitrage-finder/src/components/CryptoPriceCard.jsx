// CryptoPriceCard.jsx

import React from 'react';
import Bitcoin from "../assets/Bitcoin.png";
import Coinbase from "../assets/Coinbase.png";
import GreenArrowUp from "../assets/GreenArrowUp.png";

const CryptoPriceCard = () => {
    return (
        <div className="w-full h-full">
            <div className="flex justify-center text-2xl font-bold text-[#C2C2C2] mb-4">Exchange 1</div>

            <div className="w-full h-3/5 bg-[#2B2F38] rounded-[5px] p-2 mb-4">
                <div className="w-full h-full bg-[#373B47] rounded-[5px] p-4 flex flex-col justify-between">

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
                            <img src={GreenArrowUp} alt="Arrow Up" className="h-10 mr-2" />
                            <div className="text-white font-bold text-3xl mr-[2vw]">
                                $68,203.69
                            </div>
                        </div>

                        {/* Right Item */}
                        <div className="flex items-center">
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
                                <div class="text-[#B4B4B4] text-sm mt-2">Volume</div>
                                <div class="text-white font-semibold mb-2">$72.78B</div>
                            </div>

                            <div class="bg-[#202229] rounded-[5px] w-1/4 flex flex-col justify-center items-center">
                                <div class="text-[#B4B4B4] text-sm mt-2">Volume</div>
                                <div class="text-white font-semibold mb-2">$72.78B</div>
                            </div>

                            <div class="bg-[#202229] rounded-[5px] w-1/4 flex flex-col justify-center items-center">
                                <div class="text-[#B4B4B4] text-sm mt-2">Volume</div>
                                <div class="text-white font-semibold mb-2">$72.78B</div>
                            </div>

                            <div class="bg-[#202229] rounded-[5px] w-1/4 flex flex-col justify-center items-center">
                                <div class="text-[#B4B4B4] text-sm mt-2">Volume</div>
                                <div class="text-white font-semibold mb-2">$72.78B</div>
                            </div>

                        </div>
                    </div>

                </div>
            </div>

            <div className="w-full h-1/4 bg-[#2B2F38] rounded-[5px] p-2">
                <div className="w-full h-full bg-[#373B47] rounded-[5px] flex items-center justify-between p-12">
                    <img src={Coinbase} alt="Logo" className="h-12 ml-1" />
                    <div className="flex flex-col justify-center">
                        <div className="text-white font-semibold mr-8">Coinbase</div>
                    </div>
                    <div className="bg-[#202229] rounded-[5px] w-1/4 flex flex-col justify-center items-center mr-4">
                        <div className="text-[#B4B4B4] text-sm mt-2">Maker fee</div>
                        <div className="text-white font-semibold mb-2">0.002%</div>
                    </div>
                    <div className="bg-[#202229] rounded-[5px] w-1/4 flex flex-col justify-center items-center">
                        <div className="text-[#B4B4B4] text-sm mt-2">Taker fee</div>
                        <div className="text-white font-semibold mb-2">0.004%</div>
                    </div>
                </div>

            </div>
        </div>
    );
};

export default CryptoPriceCard;
