// src/components/Button.jsx
import React from 'react';

const Button = ({ label, onClick, className, type = 'button', isPrimary = true }) => {
  const backgroundColor = isPrimary ? 'bg-[#592FA2]' : 'bg-[#292C2F]'
  const backgroundHoveColor = isPrimary ? 'hover:bg-[#4B238D]' : 'hover:bg-[#414549]'
  return (
    <button
      type={type}
      onClick={onClick}
      className={`${backgroundColor} ${backgroundHoveColor} text-white font-medium py-2 md-lg:px-8 px-4 h-full rounded-[5px] transition duration-300  text-center ${className}`}
    >
      {label}
    </button>
  );
};

export default Button;
