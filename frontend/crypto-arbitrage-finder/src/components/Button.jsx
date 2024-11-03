// src/components/Button.jsx
import React from 'react';

const Button = ({ label, onClick, className, type = 'button', isPrimary = true, disabled = false }) => {
  const backgroundColor = disabled 
    ? 'bg-gray-500 cursor-not-allowed' // Darker disabled background color
    : isPrimary 
      ? 'bg-[#592FA2]' 
      : 'bg-[#292C2F]';

  const backgroundHoverColor = disabled 
    ? '' // No hover effect when disabled
    : isPrimary 
      ? 'hover:bg-[#4B238D]' 
      : 'hover:bg-[#414549]';

  return (
    <button
      type={type}
      onClick={disabled ? null : onClick} // Prevent click when disabled
      className={`${backgroundColor} ${backgroundHoverColor} text-white font-medium py-2 md-lg:px-8 px-4 h-full rounded-[5px] transition duration-300 text-center ${className}`}
      disabled={disabled} // Set the disabled attribute
    >
      {label}
    </button>
  );
};

export default Button;
