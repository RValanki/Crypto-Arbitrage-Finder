// src/components/ArbitragePair.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import Binance from '../assets/Binance.png';
import Coinbase from "../assets/Coinbase.png";
import Bybit from "../assets/Bybit.png"
import Huobi from "../assets/Huobi.png"
import Kucoin from "../assets/Kucoin.png"
import Kraken from "../assets/Kraken.png"
import OKX from "../assets/OKX.png"
import Bitcoin from "../assets/Bitcoin.png";
import GreenArrowUp from "../assets/GreenArrowUp.png";
import RedArrowDown from "../assets/RedArrowDown.png";

const ArbitragePair = ({ data }) => { // Accept id as a prop

    const exchangeIcons = {
        "Coinbase": Coinbase,
        "Binance": Binance,
        "Bybit": Bybit,
        "Huobi": Huobi,
        "KuCoin": Kucoin,
        "Kraken": Kraken,
        "OKX": OKX
    }

    return (
        <Link to={`/arbitragepair`}> {/* Link to the TradeInfoPage with id */}
            <div className="w-full  bg-[#2B2F38] rounded-[5px] mb-2.5 p-2 group hover:bg-[#373B47] transition-colors duration-300 ease-in-out cursor-pointer">

                <div className="animate-fadeIn flex h-full">

                    <div className="flex md-lg:flex-row flex-col mr-2 w-2/3">


                        {/* First column: 2/5 of the width */}
                        <div className="md-lg:w-1/2 w-full flex bg-[#373B47] p-2 rounded-[20px] flex items-center md-lg:mb-0 mb-2 py-4 mr-0 md-lg:mr-2 justify-center">
                            <img src={Bitcoin} alt="Logo" className="h-9 ml-1 mr-2" />
                            <div className="flex items-center justify-center text-white font-bold text-[11px]">
                                {data.symbol}
                            </div>
                            <div className="flex items-center justify-center bg-[#2B2F38] ml-2 p-2 h-[4vh] max-h-[30px] rounded-[5px] text-white text-xs">
                                <img src={exchangeIcons[data.buyExchange]} alt="Logo" className="h-6  mr-2" />
                                {data.buyExchange}
                            </div>
                            <img src={RedArrowDown} alt="Logo" className="h-2 ml-2" />
                            <div className="flex items-center justify-center text-white font-bold text-xs ml-1">
                                ${data.buyPrice}
                            </div>
                        </div>

                        {/* Second column: 2/5 of the width */}
                        <div className="md-lg:w-1/2 w-full flex bg-[#373B47] p-2 rounded-[20px] flex items-center py-4 justify-center">
                            <img src={Bitcoin} alt="Logo" className="h-9 ml-1 mr-2" />
                            <div className="flex items-center justify-center text-white font-bold text-[11px]">
                                {data.symbol}
                            </div>
                            <div className="flex items-center justify-center bg-[#2B2F38] ml-2 p-2 h-[4vh] max-h-[30px] rounded-[5px] text-white text-xs">
                                <img src={exchangeIcons[data.sellExchange]} alt="Logo" className="h-6  mr-2" />
                                {data.sellExchange}
                            </div>
                            <img src={GreenArrowUp} alt="Logo" className="h-2 ml-2" />
                            <div className="flex items-center justify-center text-white font-bold text-xs ml-1">
                                ${data.sellPrice}
                            </div>
                        </div>


                    </div>




                    {/* Third column: 1/5 of the width */}
                    <div className="md-lg:w-1/3 w-1/3 flex bg-[#373B47] p-2 rounded-[20px] flex flex-wrap justify-center">

                        <div className="flex md-lg:flex-row flex-col justify-center">

                            <div className='flex flex-row justify-center'>
                                <div className="flex items-center justify-center text-white font-semibold text-sm ml-2">
                                    Profit
                                </div>


                                <div
                                    className={`flex items-center justify-center bg-[#2B2F38] ml-2 font-bold p-2 my-1 rounded-[5px] ${data.profitPercentage === 0
                                            ? "text-gray-500" // Gray for 0
                                            : data.profitPercentage < 0
                                                ? "text-red-500" // Red for negative profit
                                                : "text-[#10A91A]" // Green for positive profit
                                        }`}
                                >
                                    {parseFloat(data.profitPercentage).toFixed(1)}%
                                </div>

                            </div>

                            <div className='flex flex-row'>
                                <div className="flex items-center justify-center text-white font-semibold text-sm ml-2">
                                    After fees
                                </div>
                                <div
                                    className={`flex items-center justify-center bg-[#2B2F38] ml-2 font-bold p-2 my-1 rounded-[5px] ${data.profitPercentageAfterFees === 0
                                            ? "text-gray-500" // Gray for 0
                                            : data.profitPercentageAfterFees < 0
                                                ? "text-red-500" // Red for negative profit
                                                : "text-[#10A91A]" // Green for positive profit
                                        }`}
                                >
                                    {parseFloat(data.profitPercentageAfterFees).toFixed(1)}%
                                </div>
                            </div>

                        </div>

                    </div>
                </div>
            </div>
        </Link>
    );
};

export default ArbitragePair;
