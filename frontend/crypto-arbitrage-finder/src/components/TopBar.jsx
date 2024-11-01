// src/components/TopBar.jsx
import React, { useEffect, useState } from 'react';
import { useLocation, Link } from 'react-router-dom'; // Import Link and useLocation
import logo from '../assets/logo.png';
import settingsIcon from '../assets/settings.png';
import Button from './Button';

const TopBar = () => {
  const [scrolled, setScrolled] = useState(false);
  const location = useLocation(); // Access current location

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
      // If already on the homepage, scroll to the top
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  return (
    <div className={`fixed top-0 left-0 right-0 p-4 text-white flex items-center bg-[#181A1F] z-50 transition-shadow duration-300 ${scrolled ? 'shadow-lg' : ''}`}>
      <div className="flex items-center mr-6">
        <img src={logo} alt="Logo" className="h-16 ml-6 mr-2" />
      </div>

      <nav className="flex items-left space-x-6">
        <ul className="flex space-x-10">
          {/* Use handleHomeClick on Home link */}
          <li>
            <Link to="/" onClick={handleHomeClick} className="hover:text-gray-400">
              Home
            </Link>
          </li>
          <li><a href="#" className="hover:text-gray-400">About</a></li>
          <li><a href="#" className="hover:text-gray-400">Contact</a></li>
          <li><a href="#" className="hover:text-gray-400">Contacts</a></li>
        </ul>
      </nav>

      <Button label="Sign Up" onClick={() => console.log('Register clicked')} className="ml-auto" isPrimary={false} />
      <Button label="Sign In" onClick={() => console.log('Sign In clicked')} className="ml-4 mr-2" />
      <img src={settingsIcon} alt="Settings" className="h-8 w-8 ml-2 mr-4 cursor-pointer hover:opacity-75" onClick={() => console.log('Settings clicked')} />
    </div>
  );
};

export default TopBar;
