import React from 'react';
import Coinbase from "../assets/Coinbase.png";
import Bitcoin from "../assets/Bitcoin.png";

const TradeLegComponent = () => {
    return (
        <div className="h-full w-full px-4">
            <div className="text-2xl font-bold text-[#C2C2C2] mb-4">Buy Trade Leg</div>
            <div className="w-full bg-[#373B47] h-[120px] rounded-[5px] flex flex-row items-center">
                <div className="flex flex-row items-center ml-8 font-bold">
                    <p className="mr-1 text-[#10A91A]">Buy</p>
                    <p className="text-white">BTC/USD from</p>
                </div>

                <div className="flex items-center justify-center bg-[#2B2F38] ml-2 p-2 h-[4vh] rounded-[5px] text-white">
                    <img src={Coinbase} alt="Logo" className="h-4 ml-1 mr-2" />
                    Coinbase
                </div>

                <div className="flex items-center mr-2">
                    <img src={Bitcoin} alt="Logo" className="h-10 ml-24 mr-2" />
                    <div className="flex flex-col">
                        <div className="text-white font-bold">Bitcoin</div>
                        <div className="text-[#B4B4B4] text-xs">BTC/USD</div>
                    </div>
                </div>

                <input
                    type="text"
                    placeholder="No. of Coins"
                    defaultValue="1" // Default value for the first input
                    className="rounded-[5px] h-10 w-32 px-4 mx-2 bg-[#D9D9D9] text-black border border-transparent focus:outline-none focus:border-blue-500"
                />

                <div className="text-white font-bold mx-4">
                    for
                </div>

                <input
                    type="text"
                    placeholder="Price of coin"
                    defaultValue="$68,203.69" // Default value for the second input
                    className="rounded-[5px] h-10 w-32 px-4 mx-2 bg-[#D9D9D9] text-black border border-transparent focus:outline-none focus:border-blue-500"
                />
            </div>
        </div>
    );
};

export default TradeLegComponent;
