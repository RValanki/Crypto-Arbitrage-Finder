// src/components/Button.jsx
import React from 'react';

const Button = ({ label, onClick, className, type = 'button' }) => {
  return (
    <button
      type={type}
      onClick={onClick}
      className={`bg-[#592FA2] text-white font-medium py-2 px-8 h-full rounded-[5px] transition duration-300 hover:bg-[#4B238D] text-center ${className}`}
    >
      {label}
    </button>
  );
};

export default Button;
