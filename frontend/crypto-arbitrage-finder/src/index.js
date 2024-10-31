// src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './styling/index.css'; // Import global styles
import './styling/App.css'; // Import additional styles
import HomePage from './pages/HomePage'; // Import HomePage from the pages directory
import TradeInfoPage from './pages/TradeInfoPage';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} /> {/* Set HomePage as the default route */}
        <Route path="/arbitragepair" element={<TradeInfoPage />}/> 
        {/* Add other routes here if you have other pages */}
        {/* <Route path="/app" element={<App />} /> */}
      </Routes>
    </Router>
  </React.StrictMode>
);


