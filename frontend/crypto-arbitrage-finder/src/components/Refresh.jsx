import React from 'react';
import Button from './Button';

const Refresh = ({ onRefresh }) => {
  return (
    <div className="w-full h-full p-3 flex flex-col items-center max-h-[150px] min-w-[290px]"> {/* Set max height */}
      <Button 
        label="Refresh" 
        onClick={onRefresh} 
        className="font-bold w-full h-2/3" 
      />
      <p className="text-white text-xs text-center mt-2"> {/* Center align the text */}
        Last Updated at: 8:38:45 PM
      </p>
    </div>
  );
};

export default Refresh;
