import React, { useEffect, useState } from 'react';
import { useLocation, Link } from 'react-router-dom';
import logo from '../assets/logo.png';
import settingsIcon from '../assets/settings.png';
import Button from './Button';
import AlertBanner from '../components/AlertBanner'; // Import the AlertBanner component
import { FaHome, FaInfoCircle, FaEnvelope, FaPhone, FaUserPlus, FaSignInAlt } from 'react-icons/fa'; // Example with react-icons

const TopBar = ({ showAlert, setShowAlert }) => { // Accept showAlert and setShowAlert as props
  const [scrolled, setScrolled] = useState(false);
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const location = useLocation();

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
      
      <div className={` border-b-[0.1px] md-lg:border-[#323336] border-[#323336] fixed top-0 left-0 right-0 p-4 text-white flex items-center bg-[#181A1F] z-50 transition-shadow duration-300 ${scrolled ? 'shadow-lg' : ''}`}>
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
              <div className="sm:absolute sm:left-0 absolute right-0 mt-2 w-48 bg-gray-800 text-white rounded-lg shadow-lg py-2">
                <Link to="/" onClick={handleHomeClick} className="block px-4 py-2 hover:bg-gray-700">
                  Home
                </Link>
                <Link to="/about" className="block px-4 py-2 hover:bg-gray-700">
                  About
                </Link>
                <Link to="/contact" className="block px-4 py-2 hover:bg-gray-700">
                  Contact
                </Link>
                <Link to="/contacts" className="block px-4 py-2 hover:bg-gray-700">
                  Contacts
                </Link>
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
