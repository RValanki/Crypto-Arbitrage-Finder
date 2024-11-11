import React from 'react';
import Coinbase from "../assets/Coinbase.png";
import Bitcoin from "../assets/Bitcoin.png";

const TradeLegComponent = () => {
    return (
        <div className="h-full w-full px-4 md-lg:min-w-[910px] min-w-[0px]">
            <div className="text-2xl font-bold text-[#C2C2C2] mb-4">Buy Trade Leg</div>
            <div className="w-full bg-[#2B2F38] md-lg:min-h-[120px] min-h-[150px] rounded-[5px] flex md-lg:flex-row flex-col items-center justify-center">
            
                <div className="flex md-lg:flex-row md-lg:mb-0 mb-4 md-lg:mt-0 mt-6">

                
                <div className="flex flex-row items-center ml-8 font-bold">
                    <p className="mr-1 text-[#10A91A]">Buy</p>
                    <p className="text-white">BTC/USD from</p>
                </div>

                <div className="flex items-center justify-center bg-[#202229] ml-2 p-2 h-[4vh] rounded-[5px] text-white">
                    <img src={Coinbase} alt="Logo" className="h-4 ml-1 mr-2" />
                    Coinbase
                </div>
                </div>


                <div className="flex md-lg:flex-row md-lg:mb-0 mb-4">
                <div className="flex items-center mr-2">
                    <img src={Bitcoin} alt="Logo" className="h-10 ml-[4vw] mr-2" />
                    <div className="flex flex-col">
                        <div className="text-white font-bold">Bitcoin</div>
                        <div className="text-[#B4B4B4] text-xs">BTC/USD</div>
                    </div>
                </div>

                <input
                    type="text"
                    placeholder="No. of Coins"
                    defaultValue="1" // Default value for the first input
                    className="rounded-[5px] h-10 w-32 px-4 mx-2 bg-[#D9D9D9] text-black border border-transparent focus:outline-none focus:border-[#592FA2]"
                />

                <div className="text-white font-bold mx-4 mt-2">
                    for
                </div>

                <input
                    type="text"
                    placeholder="Price of coin"
                    defaultValue="$68,203.69" // Default value for the second input
                    className="rounded-[5px] h-10 w-32 px-4 mx-2 bg-[#D9D9D9] text-black border border-transparent focus:outline-none focus:border-[#592FA2]"
                />

            </div>
            </div>
        </div>
    );
};

export default TradeLegComponent;
