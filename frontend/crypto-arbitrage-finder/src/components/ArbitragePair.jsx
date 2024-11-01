// src/components/ArbitragePair.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import Binance from '../assets/Binance.png';
import CoinBase from "../assets/Coinbase.png";
import Bitcoin from "../assets/Bitcoin.png";
import GreenArrowUp from "../assets/GreenArrowUp.png";
import RedArrowDown from "../assets/RedArrowDown.png";

const ArbitragePair = () => { // Accept id as a prop
    return (
        <Link to={`/arbitragepair`}> {/* Link to the TradeInfoPage with id */}
            <div className="w-full h-[10vh] bg-[#2B2F38] rounded-[5px] mb-2.5 p-2 group hover:bg-[#373B47] transition-colors duration-300 ease-in-out cursor-pointer">
                <div className="animate-fadeIn flex h-full">
                    {/* First column: 2/5 of the width */}
                    <div className="flex-[3] bg-[#373B47] p-2 rounded-[20px] flex items-center">
                        <img src={Bitcoin} alt="Logo" className="h-9 ml-1 mr-2" />
                        <div className="flex items-center justify-center text-white font-bold text-xs">
                            BTC/USD
                        </div>
                        <div className="flex items-center justify-center bg-[#2B2F38] ml-2 p-2 h-[4vh] rounded-[5px] text-white">
                            <img src={CoinBase} alt="Logo" className="h-4 ml-1 mr-2" />
                            Coinbase
                        </div>
                        <img src={RedArrowDown} alt="Logo" className="h-2 ml-2" />
                        <div className="flex items-center justify-center text-white font-bold text-xs ml-1">
                            $68,203.69
                        </div>
                    </div>

                    {/* Second column: 2/5 of the width */}
                    <div className="flex-[3] bg-[#373B47] p-2 rounded-[20px] mx-2 flex items-center">
                        <img src={Bitcoin} alt="Logo" className="h-9 ml-1 mr-2" />
                        <div className="flex items-center justify-center text-white font-bold text-xs">
                            BTC/USD
                        </div>
                        <div className="flex items-center justify-center bg-[#2B2F38] ml-2 p-2 h-[4vh] rounded-[5px] text-white">
                            <img src={Binance} alt="Logo" className="h-4 ml-1 mr-2" />
                            Binance
                        </div>
                        <img src={GreenArrowUp} alt="Logo" className="h-2 ml-2" />
                        <div className="flex items-center justify-center text-white font-bold text-xs ml-1">
                            $68,523.89
                        </div>
                    </div>

                    {/* Third column: 1/5 of the width */}
                    <div className="flex-[2.5] bg-[#373B47] p-2 rounded-[20px] flex flex-wrap ">
                        <div className="flex items-center justify-center text-white font-semibold text-sm ml-2">
                            Profit
                        </div>
                        <div className="flex items-center justify-center bg-[#2B2F38] ml-2 font-bold p-2 my-1 rounded-[5px] text-[#10A91A]">
                            2.3%
                        </div>
                        <div className="flex items-center justify-center text-white font-semibold text-sm ml-2">
                            After fees
                        </div>
                        <div className="flex items-center justify-center bg-[#2B2F38] ml-2 font-bold p-2 my-1 rounded-[5px] text-[#10A91A]">
                            1.1%
                        </div>
                    </div>
                </div>
            </div>
        </Link>
    );
};

export default ArbitragePair;
