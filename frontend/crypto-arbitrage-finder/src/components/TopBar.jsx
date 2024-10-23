// src/components/TopBar.jsx
import React, { useEffect, useState } from 'react';
import logo from '../assets/logo.png'; 
import settingsIcon from '../assets/settings.png'; // Import the settings icon
import Button from './Button'; // Import the Button component

const TopBar = () => {
  const [scrolled, setScrolled] = useState(false);

  const handleScroll = () => {
    // Check if the user has scrolled down 50 pixels
    if (window.scrollY > 50) {
      setScrolled(true);
    } else {
      setScrolled(false);
    }
  };

  useEffect(() => {
    // Attach the scroll event listener
    window.addEventListener('scroll', handleScroll);
    // Cleanup the event listener on component unmount
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <div className={`fixed top-0 left-0 right-0 p-4 text-white flex items-center bg-[#181A1F] z-50 transition-shadow duration-300 ${scrolled ? 'shadow-lg' : ''}`}>
      <div className="flex items-center mr-6">
        <img src={logo} alt="Logo" className="h-16 ml-6 mr-2" /> 
      </div>

      <nav className="flex items-left space-x-6"> 
        <ul className="flex space-x-10">
          <li><a href="#" className="hover:text-gray-400">Home</a></li>
          <li><a href="#" className="hover:text-gray-400">About</a></li>
          <li><a href="#" className="hover:text-gray-400">Contact</a></li>
          <li><a href="#" className="hover:text-gray-400">Contacts</a></li>
        </ul>
      </nav>

      {/* Swapped Button components with updated color */}
      <Button label="Sign Up" onClick={() => console.log('Register clicked')} className="ml-auto" isPrimary = {false} />
      <Button label="Sign In" onClick={() => console.log('Sign In clicked')} className="ml-4 mr-2" />

      {/* Settings icon next to Sign In button */}
      <img src={settingsIcon} alt="Settings" className="h-8 w-8 ml-2 mr-4 cursor-pointer hover:opacity-75" onClick={() => console.log('Settings clicked')} />
    </div>
  );
};

export default TopBar;
