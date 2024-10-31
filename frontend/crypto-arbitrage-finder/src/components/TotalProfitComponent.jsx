import React from 'react';
import GreenArrowUp from "../assets/GreenArrowUp.png"

const TotalProfitComponent = () => {
    return (
        <div className="h-full w-full px-4 flex flex-col items-center">
            <div className="text-2xl font-bold text-white mb-4">Total Profit from trade</div>
            <div className="w-1/2 bg-[#2B2F38] h-[120px] rounded-[5px] p-2">
                <div className="w-full bg-[#373B47] h-full rounded-[5px] flex justify-center items-center"> {/* Center the items */}

                    <div className="bg-[#202229] rounded-[5px] w-1/3 flex flex-col justify-center items-center mx-2 h-3/4"> {/* Add h-full for full height */}
                        <div className="text-white font-semibold text-xl"> {/* Remove m-8 to prevent additional spacing */}
                            $320.30
                        </div>
                    </div>

                    <div className="bg-[#202229] rounded-[5px] w-1/3 flex flex-row justify-center items-center mx-2 h-3/4"> {/* Change to flex-row */}
                        <img src={GreenArrowUp} alt="Arrow Up" className="h-4 mr-1" />
                        <div className="text-white font-semibold text-xl mr-2">
                            2%
                        </div>
                    </div>



                </div>
            </div>
        </div>
    );
};

export default TotalProfitComponent;
