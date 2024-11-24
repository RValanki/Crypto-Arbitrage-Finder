import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import logo from './logo.svg'; // Assuming you have a logo.svg
import './styling/App.css'; // Keep this to include any specific styles
import HomePage from './pages/HomePage'; // Import the HomePage component
import TradeInfoPage from './pages/TradeInfoPage'
import ScrollToTop from './components/ScrollToTop';

function App() {
  return (
    <Router>
      <ScrollToTop />
      <div className="App flex flex-col items-center justify-center min-h-screen text-white bg-gray-800">
        <header className="App-header flex flex-col items-center justify-center">
          <img
            src={logo}
            className="App-logo h-[40vmin] pointer-events-none"
            alt="logo"
          />
          <p className="text-xl">
            Edit <code className="text-blue-400">src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link text-blue-400 hover:text-blue-300"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>

        {/* Define the routes */}
        <Routes>
          
          
        </Routes>
      </div>
    </Router>
  );
}

export default App;
