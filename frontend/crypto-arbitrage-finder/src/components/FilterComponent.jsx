import React, { useState, useEffect } from 'react';
import PurpleArrow from "../assets/PurpleArrow.png";
import GreyArrow from "../assets/GreyArrow.png";

const FilterComponent = ({ defaultValue, options, selected = false }) => {
  const [isOpen, setIsOpen] = useState(false); // State to control dropdown visibility
  const [selectedOption, setSelectedOption] = useState(null); // Set the initial selected option

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

  // Update selectedOption when the selected prop changes
  useEffect(() => {
    setSelectedOption(selected ? defaultValue : null);
  }, [selected, defaultValue]);

  // Determine the background color based on the selected option
  const backgroundColor = selectedOption ? '#373B47' : '#24262B';

  return (
    <div 
      className={`w-full h-full bg-[${backgroundColor}] rounded-[3px] hover:bg-[#373B47] transition-colors duration-300 ease-in-out flex items-center relative cursor-pointer`}
      onClick={toggleDropdown}
    >
      {/* Centered text */}
      <div className="text-white text-xs mx-auto">
        {selectedOption || defaultValue || "Sort by largest marketcap"}
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
            {options.map((option, index) => (
              <li 
                key={index} 
                className="py-1 hover:bg-[#2B2F38] px-2 rounded" 
                onClick={() => handleOptionClick(option)}
              >
                {option}
              </li>
            ))}
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
