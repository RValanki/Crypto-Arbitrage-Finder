// src/components/AlertBanner.jsx
import React from 'react';

const AlertBanner = ({ message, type, onClose }) => {
  const alertClasses = {
    success: 'bg-green-100 border-green-400 text-green-700',
    error: 'bg-red-100 border-red-400 text-red-700',
    warning: 'bg-yellow-100 border-yellow-400 text-yellow-700',
    info: 'bg-blue-100 border-blue-400 text-blue-700',
  };

  return (
    <div className={`border-l-4 p-6 ${alertClasses[type]} rounded m-2`} role="alert">
      <div className="flex justify-between items-start">
        <div>{message}</div>
      </div>
    </div>
  );
};

export default AlertBanner;
