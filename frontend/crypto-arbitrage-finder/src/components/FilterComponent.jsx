import React from 'react';
import PurpleArrow from "../assets/PurpleArrow.png";

const FilterComponent = () => {
  return (
    <div className="w-full h-full bg-[#24262B] rounded-[3px] hover:bg-[#373B47] transition-colors duration-300 ease-in-out flex items-center relative">
      {/* Centered text */}
      <div className="text-white text-xs mx-auto">
        Sort by largest marketcap
      </div>
      {/* Right aligned image */}
      <img src={PurpleArrow} alt="Logo" className="h-3 absolute right-2" />
    </div>
  );
};

export default FilterComponent;
