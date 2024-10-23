import React, { useState } from 'react';
import PurpleArrow from "../assets/PurpleArrow.png";
import GreyArrow from "../assets/GreyArrow.png";

const FilterComponent = () => {
  const [isOpen, setIsOpen] = useState(false); // State to control dropdown visibility
  const [selectedOption, setSelectedOption] = useState(null); // State to track selected option

  const toggleDropdown = () => {
    setIsOpen(!isOpen); // Toggle the dropdown on click
  };

  const handleOptionClick = (option) => {
    if (option === "Deselect") {
      setSelectedOption(null); // Deselect the filter
    } else {
      setSelectedOption(option); // Set the selected option
    }
    setIsOpen(false); // Close the dropdown
  };

  // Determine the background color based on the selected option
  const backgroundColor = selectedOption ? '#373B47' : '#24262B';

  return (
    <div 
      className={`w-full h-full bg-[${backgroundColor}] rounded-[3px] hover:bg-[#373B47] transition-colors duration-300 ease-in-out flex items-center relative cursor-pointer`}
      onClick={toggleDropdown}
    >
      {/* Centered text */}
      <div className="text-white text-xs mx-auto">
        {selectedOption ? selectedOption : "Sort by largest marketcap"}
      </div>
      {/* Right aligned image */}
      <img 
        src={selectedOption ? PurpleArrow : GreyArrow} 
        alt="Arrow" 
        className="h-3 absolute right-2" 
      />

      {/* Dropdown */}
      {isOpen && (
        <div className="absolute top-full mt-2 w-full bg-[#373B47] rounded-md shadow-lg z-10">
          <ul className="text-white text-xs p-2">
            <li 
              className="py-1 hover:bg-[#2B2F38] px-2 rounded" 
              onClick={() => handleOptionClick("Option 1")}
            >
              Option 1
            </li>
            <li 
              className="py-1 hover:bg-[#2B2F38] px-2 rounded" 
              onClick={() => handleOptionClick("Option 2")}
            >
              Option 2
            </li>
            <li 
              className="py-1 hover:bg-[#2B2F38] px-2 rounded" 
              onClick={() => handleOptionClick("Option 3")}
            >
              Option 3
            </li>
            <li 
              className="py-1 hover:bg-[#2B2F38] px-2 rounded" 
              onClick={() => handleOptionClick("Deselect")}
            >
              Deselect
            </li>
          </ul>
        </div>
      )}
    </div>
  );
};

export default FilterComponent;
