// src/components/Filters.jsx
import React from 'react';
import FilterComponent from './FilterComponent';

const Filters = () => {
  return (
    <div class = "w-full h-full">
        <div class = "ml-4 mt-2 text-white font-bold">
            Filters
        </div>
        <div class = "h-[5vh] mx-4 mt-3">
            <FilterComponent 
                defaultValue="Sort by highest profit" 
                options={["Sort by highest profit", "Sort by lowest profit", "Sort by highest profit after fees", "Sort by lowest profit after fees"]} 
                selected={true}
            />
        </div>
        <div class = "h-[5vh] mx-4 mt-3">
            <FilterComponent 
                defaultValue="Show first 20" 
                options={["Show first 20", "Show first 50", "Show first 100", "Show All"]} 
                selected={true}
            />
        </div>
        <div class = "h-[5vh] mx-4 mt-3">
             <FilterComponent 
                defaultValue="Sort by largest marketcap" 
                options={["Sort by largest marketcap", "Sort by smallest marketcap"]} 
            />  
        </div>
        <div class = "h-[5vh] mx-4 mt-3">
            <FilterComponent 
                defaultValue="Trade Specific Cryptos" 
                options={["Trade Specific Cryptos"]} 
            />
        </div>
        
    </div>
  );
};

export default Filters;
