  // src/pages/HomePage.jsx
  import React from 'react';
  import TopBar from '../components/TopBar'; // Adjust the import path as necessary
  import Refresh from '../components/Refresh';
  import ArbitragePair from '../components/ArbitragePair';
  import Filters from '../components/Filters';
  import AboutComponent from '../components/AboutComponent';

  const HomePage = () => {
    return (
      <div>
        <TopBar /> {/* Add the TopBar component here */}

        <h1 className="w-full h-[10vh] text-white font-bold sm:text-5xl text-4xl md-lg:text-left text-center md-lg:ml-32 ml-0 mt-32">
          Crypto Arbitrage Finder
        </h1>


        {/* Flexbox layout with two columns */}
        <div className="flex mt-10 md-lg:ml-20 md-lg:mr-20"> {/* Add margin-top for spacing */}
          {/* First Column (3/4 width) */}

          <div className="flex md-lg:flex-row flex-col">
          <div className="flex-[5] p-4 sm:px-12 md-lg:px-4 px-4">
            <h2 className="text-white">First Column</h2>

            <div className="w-full   bg-[#1F2025] rounded-[5px] p-2 md-lg:min-w-[1000px] min-w-[500px]">
              {/* Content for the first column */}


              <ArbitragePair> </ArbitragePair>
              <ArbitragePair> </ArbitragePair>
              <ArbitragePair> </ArbitragePair>
              <ArbitragePair> </ArbitragePair>
              <ArbitragePair> </ArbitragePair>
              <ArbitragePair> </ArbitragePair>
              <ArbitragePair> </ArbitragePair>
              <ArbitragePair> </ArbitragePair>
              <ArbitragePair> </ArbitragePair>
              <ArbitragePair> </ArbitragePair>
              <ArbitragePair> </ArbitragePair>
              <ArbitragePair> </ArbitragePair>
              <ArbitragePair> </ArbitragePair>


            </div>
          </div>

          {/* Second Column (1/4 width) */}
          <div className="flex-[1.6] p-4 flex flex-col sm:px-16 md-lg:px-0">


            {/* Three Rows in Second Column */}
            <div className=" h-[15vh] bg-[#1F2025] rounded-[5px] mt-6 mb-4 p-2">
              <Refresh> </Refresh>
            </div>
            <div className="h-[35vh] bg-[#1F2025] rounded-[5px] mb-4 p-2">
              <Filters> </Filters>
            </div>
            <div className=" h-[50vh] bg-[#1F2025] rounded-[5px] p-2">
              <AboutComponent> </AboutComponent>
            </div>
          </div>
          </div>
          
        </div>
      </div>
    );
  };

  export default HomePage;
