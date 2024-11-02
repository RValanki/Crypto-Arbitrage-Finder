// src/components/TopBar.jsx
import React, { useEffect, useState } from 'react';
import { useLocation, Link } from 'react-router-dom';
import logo from '../assets/logo.png';
import settingsIcon from '../assets/settings.png';
import Button from './Button';
import AlertBanner from '../components/AlertBanner'; // Import the AlertBanner component
import { FaHome, FaInfoCircle, FaEnvelope, FaPhone, FaUserPlus, FaSignInAlt } from 'react-icons/fa'; // Example with react-icons

const TopBar = () => {
  const [scrolled, setScrolled] = useState(false);
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const location = useLocation();
  
  const [showAlert, setShowAlert] = useState(true);

  const handleCloseAlert = () => setShowAlert(false);

  const handleScroll = () => {
    setScrolled(window.scrollY > 50);
  };

  useEffect(() => {
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  useEffect(() => {
    if (showAlert) {
      const timer = setTimeout(() => {
        setShowAlert(false);
      }, 2000); // Close alert after 2 seconds

      return () => clearTimeout(timer); // Cleanup timer on component unmount or alert close
    }
  }, [showAlert]);

  const handleHomeClick = () => {
    if (location.pathname === "/") {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  const toggleDropdown = () => {
    setDropdownOpen(!dropdownOpen);
  };

  return (
    <>
      {/* Alert Banner */}
      {showAlert && (
        <div style={{ position: 'fixed', top: 0, left: 0, right: 0, zIndex: 60 }}>
          <AlertBanner
            message="Refreshed Successfully!"
            type="info" // Change to "error", "warning", or "info" as needed
            onClose={handleCloseAlert}
          />
        </div>
      )}

      <div className={`md-lg:border-b-[0px] border-b-[0.1px] md-lg:border-[#323336] border-[#323336] fixed top-0 left-0 right-0 p-4 text-white flex items-center bg-[#181A1F] z-50 transition-shadow duration-300 ${scrolled ? 'shadow-lg' : ''}`}>
        <div className="flex items-center">
          <img src={logo} alt="Logo" className="h-16 ml-6 md-lg:mr-8 mr-0" />
        </div>

        <nav className="flex-grow">
          <ul className="hidden md-lg:flex space-x-10">
            <li>
              <Link to="/" onClick={handleHomeClick} className="flex items-center hover:text-gray-400">
                Home
              </Link>
            </li>
            <li>
              <Link to="/about" className="flex items-center hover:text-gray-400">
                About
              </Link>
            </li>
            <li>
              <Link to="/contact" className="flex items-center hover:text-gray-400">
                Contact
              </Link>
            </li>
            <li>
              <Link to="/contacts" className="flex items-center hover:text-gray-400">
                Contacts
              </Link>
            </li>
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
                    <Link to="/" onClick={handleHomeClick} className="flex items-center block px-4 py-2 text-white hover:bg-gray-700">
                      <FaHome className="mr-2" /> Home
                    </Link>
                  </li>
                  <li>
                    <Link to="/about" className="flex items-center block px-4 py-2 text-white hover:bg-gray-700">
                      <FaInfoCircle className="mr-2" /> About
                    </Link>
                  </li>
                  <li>
                    <Link to="/contact" className="flex items-center block px-4 py-2 text-white hover:bg-gray-700">
                      <FaEnvelope className="mr-2" /> Contact
                    </Link>
                  </li>
                  <li>
                    <Link to="/contacts" className="flex items-center block px-4 py-2 text-white hover:bg-gray-700">
                      <FaEnvelope className="mr-2" /> Contacts
                    </Link>
                  </li>

                  <div className="sm:hidden">
                    <li>
                      <Link to="/signup" className="flex items-center block px-4 py-2 text-white hover:bg-gray-700">
                        <FaUserPlus className="mr-2" /> Sign Up
                      </Link>
                    </li>
                    <li>
                      <Link to="/signin" className="flex items-center block px-4 py-2 text-white hover:bg-gray-700">
                        <FaSignInAlt className="mr-2" /> Sign In
                      </Link>
                    </li>
                    <li>
                      <a href="#" className="flex items-center block px-4 py-2 text-white hover:bg-gray-700">
                        <img src={settingsIcon} alt="Settings" className="h-4 w-4 mr-2" /> Settings
                      </a>
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
    </>
  );
};

export default TopBar;
