import React, { useState, useEffect } from 'react';
import TopBar from '../components/TopBar';
import Refresh from '../components/Refresh';
import ArbitragePair from '../components/ArbitragePair';
import Filters from '../components/Filters';
import AboutComponent from '../components/AboutComponent';
import { fetchArbitrageOpportunities } from '../api/arbitrageService';

const HomePage = () => {
  const [arbitrageData, setArbitrageData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetchArbitrageOpportunities();
        console.log(response); // Log to check the structure
        if (response && response.data && Array.isArray(response.data)) {
          setArbitrageData(response.data);
        } else {
          setArbitrageData([]);
        }
      } catch (error) {
        setError("Error fetching arbitrage opportunities.");
        console.error(error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <TopBar />
      <h1 className="w-full h-[10vh] text-white font-bold text-5xl md-lg:text-left text-center md-lg:ml-32 ml-0 mt-32">
        Crypto Arbitrage Finder
      </h1>

      <div className="flex mt-10 md-lg:ml-20 md-lg:mr-20">
        {/* First Column */}
        <div className="flex md-lg:flex-row flex-col">
          <div className="flex-[5] p-4 sm:px-12 md-lg:px-4 px-4">
            <div className="flex flex-row">
              <h2 className="md-lg:block hidden text-white w-1/3 flex justify-center font-semibold text-center ">Exchange 1</h2>
              <h2 className="md-lg:hidden block text-white w-2/3 flex justify-center font-semibold text-center">Exchanges</h2>
              <h2 className="md-lg:block hidden text-white w-1/3 flex justify-center font-semibold text-center">Exchange 2</h2>
              <h2 className="text-white w-1/3 flex justify-center font-semibold">Profit</h2>
            </div>

            <div className="w-full bg-[#1F2025] rounded-[5px] p-2 md-lg:min-w-[1000px] min-w-[500px]">
              {isLoading ? (
                <p className="text-white text-center mt-20 mb-80">Loading...</p>
              ) : error ? (
                <p className="text-red-500 text-center">{error}</p>
              ) : (
                Array.isArray(arbitrageData) && arbitrageData.length > 0 ? (
                  arbitrageData.map((pair, index) => (
                    <ArbitragePair key={index} data={pair} />
                  ))
                ) : (
                  <p className="text-white text-center">No arbitrage opportunities available.</p>
                )
              )}
            </div>
          </div>

          {/* Second Column */}
          <div className="flex-[1.6] p-4 flex flex-col sm:px-16 md-lg:px-0">
            <div className="h-[15vh] bg-[#1F2025] rounded-[5px] mt-6 mb-4 p-2">
              <Refresh />
            </div>
            <div className="h-[35vh] bg-[#1F2025] rounded-[5px] mb-4 p-2">
              <Filters />
            </div>
            <div className="h-[50vh] bg-[#1F2025] rounded-[5px] p-2">
              <AboutComponent />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
