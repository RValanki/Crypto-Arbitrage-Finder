// src/components/TopBar.jsx
import React, { useEffect, useState } from 'react';
import { useLocation, Link } from 'react-router-dom';
import logo from '../assets/logo.png';
import settingsIcon from '../assets/settings.png';
import Button from './Button';

const TopBar = () => {
  const [scrolled, setScrolled] = useState(false);
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const location = useLocation();

  const handleScroll = () => {
    if (window.scrollY > 50) {
      setScrolled(true);
    } else {
      setScrolled(false);
    }
  };

  useEffect(() => {
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleHomeClick = () => {
    if (location.pathname === "/") {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  const toggleDropdown = () => {
    setDropdownOpen(!dropdownOpen);
  };

  return (
    <div className={`fixed top-0 left-0 right-0 p-4 text-white flex items-center bg-[#181A1F] z-50 transition-shadow duration-300 ${scrolled ? 'shadow-lg' : ''}`}>
      <div className="flex items-center">
        <img src={logo} alt="Logo" className="h-16 ml-6 md-lg:mr-2 mr-0" />
      </div>

      <nav className="flex-grow">
        <ul className="hidden md-lg:flex space-x-10">
          <li>
            <Link to="/" onClick={handleHomeClick} className="hover:text-gray-400">
              Home
            </Link>
          </li>
          <li><a href="#" className="hover:text-gray-400">About</a></li>
          <li><a href="#" className="hover:text-gray-400">Contact</a></li>
          <li><a href="#" className="hover:text-gray-400">Contacts</a></li>
        </ul>

        {/* Dropdown for smaller screens */}
        <div className="relative md-lg:hidden flex sm:justify-between justify-end ml-4 mr-4">
          <button 
            onClick={toggleDropdown} 
            className="flex items-center hover:text-gray-400 focus:outline-none"
          >
            Menu
            <svg 
              className={`ml-2 w-4 h-4 transform transition-transform duration-200 ${dropdownOpen ? 'rotate-180' : ''}`} 
              xmlns="http://www.w3.org/2000/svg" 
              fill="none" 
              viewBox="0 0 24 24" 
              stroke="currentColor"
            >
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16m-7 6h7" />
            </svg>
          </button>
          {dropdownOpen && (
            <div className="sm:absolute sm:left-0 absolute right-0 mt-8 w-48 bg-[#2B2F38] rounded-md shadow-lg z-10">
              <ul className="py-1">
                <li>
                  <Link to="/" onClick={handleHomeClick} className="block px-4 py-2 text-white hover:bg-gray-700">
                    Home
                  </Link>
                </li>
                <li>
                  <a href="#" className="block px-4 py-2 text-white hover:bg-gray-700">About</a>
                </li>
                <li>
                  <a href="#" className="block px-4 py-2 text-white hover:bg-gray-700">Contact</a>
                </li>
                <li>
                  <a href="#" className="block px-4 py-2 text-white hover:bg-gray-700">Contacts</a>
                </li>

                <div className="sm:hidden">
                <li>
                  <a href="#" className="block px-4 py-2 text-white hover:bg-gray-700">Sign Up</a>
                </li>
                <li>
                  <a href="#" className="block px-4 py-2 text-white hover:bg-gray-700">Sign In</a>
                </li>
                <li>
                  <a href="#" className="block px-4 py-2 text-white hover:bg-gray-700">Settings</a>
                </li>
                </div>
                
              </ul>
            </div>
          )}
        </div>
      </nav>

      {/* Buttons and Settings Icon (hidden on small screens) */}
      <div className="hidden sm:flex items-center ml-auto">
        <Button label="Sign Up" onClick={() => console.log('Register clicked')} className="ml-auto" isPrimary={false} />
        <Button label="Sign In" onClick={() => console.log('Sign In clicked')} className="ml-4 mr-2" />
        <img src={settingsIcon} alt="Settings" className="h-8 w-8 ml-2 mr-4 cursor-pointer hover:opacity-75" onClick={() => console.log('Settings clicked')} />
      </div>
    </div>
  );
};

export default TopBar;
