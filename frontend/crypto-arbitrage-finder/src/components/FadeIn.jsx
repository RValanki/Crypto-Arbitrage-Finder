// src/components/FadeIn.jsx
import React from 'react';

const FadeIn = ({ children }) => {
    return (
        <div className="opacity-0 animate-fadeIn transition-opacity duration-1000 ease-in-out">
            {children}
        </div>
    );
};

export default FadeIn;
