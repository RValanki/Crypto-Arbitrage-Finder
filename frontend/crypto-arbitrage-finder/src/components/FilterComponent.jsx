import React from 'react';
import PurpleArrow from "../assets/PurpleArrow.png"

const FilterComponent = () => {
  return (
    <div className="w-full h-full bg-[#24262B] rounded-[3px] hover:bg-[#373B47] transition-colors duration-300 ease-in-out flex items-center justify-center">
      {/* Content for the filter component */}
      <div className="text-white text-xs">
        Sort by largest marketcap
      </div>
      <img src={PurpleArrow} alt="Logo" className="h-2 ml-2" />
    </div>
  );
};

export default FilterComponent;
