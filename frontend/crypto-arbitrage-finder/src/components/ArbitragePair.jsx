// src/components/ArbitragePair.jsx
import React from 'react';

const ArbitragePair = ({ label, onClick, className, type = 'button' }) => {
  return (
    <div className="w-full h-[10vh] bg-[#2B2F38] rounded-[5px] mb-2.5 p-2 group hover:bg-[#373B47] transition-colors duration-100">
      <div className="flex h-full">
        {/* First column: 2/5 of the width */}
        <div className="flex-[3] bg-[#373B47] p-2 rounded-[20px]">
          {/* Content for the first column */}
        
        </div>

        {/* Second column: 2/5 of the width */}
        <div className="flex-[3] bg-[#373B47] p-2 rounded-[20px] mx-2">
          {/* Content for the second column */}
          
        </div>

        {/* Third column: 1/5 of the width */}
        <div className="flex-[2] bg-[#373B47] p-2 rounded-[20px]">
          {/* Content for the third column */}
            
        </div>
      </div>
    </div>
  );
};

export default ArbitragePair;
