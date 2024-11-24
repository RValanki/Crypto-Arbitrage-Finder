import React from 'react';
import Button from './Button';

const Refresh = ({ onRefresh, isLoading }) => {
  return (
    <div className="w-full h-full p-3 flex flex-col items-center max-h-[150px] min-w-[290px]"> {/* Set max height */}
      <Button 
        label={isLoading ? "Refreshing..." : "Refresh"} // Update the label based on loading state
        onClick={onRefresh} 
        className="font-bold w-full h-2/3"
        disabled={isLoading} // Disable the button while loading
      />
      <p className="text-white text-xs text-center mt-2">
        Last Updated at: {new Date().toLocaleTimeString()} {/* Display dynamic time */}
      </p>
    </div>
  );
};

export default Refresh;
