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
            <FilterComponent> </FilterComponent>
        </div>
        <div class = "h-[5vh] mx-4 mt-3">
            <FilterComponent> </FilterComponent>
        </div>
        <div class = "h-[5vh] mx-4 mt-3">
            <FilterComponent> </FilterComponent>
        </div>
        <div class = "h-[5vh] mx-4 mt-3">
            <FilterComponent> </FilterComponent>
        </div>
        
    </div>
  );
};

export default Filters;
