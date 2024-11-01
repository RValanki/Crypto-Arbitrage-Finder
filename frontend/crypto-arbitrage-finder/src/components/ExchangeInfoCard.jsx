import React from 'react';
import Coinbase from "../assets/Coinbase.png";

const ExchangeInfoCard = () => {
    return (
        <div className="w-full h-1/4 bg-[#1F2025] rounded-[5px] p-2 md-lg:min-w-[430px]">
                <div className="w-full h-full bg-[#2B2F38] rounded-[5px] flex items-center justify-between p-12">
                    <img src={Coinbase} alt="Logo" className="h-12 ml-1" />
                    <div className="flex flex-col justify-center">
                        <div className="text-white font-semibold md-lg:mr-8 mr-4">Coinbase</div>
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
    );
};

export default ExchangeInfoCard;
