    // CryptoPriceCard.jsx

    import React from 'react';

    const CryptoPriceCard = () => {
    return (
        <div class = "w-full h-full">
            <div class = "flex justify-center text-2xl font-bold text-[#C2C2C2] mb-4" >Exchange 1</div>
            <div class = "w-full h-2/3 bg-[#2B2F38] rounded-[5px] p-2 mb-4">
                <div class = "w-full h-full bg-[#373B47] rounded-[5px]">  </div>
            </div>

            <div class = "w-full h-1/3 bg-[#2B2F38] rounded-[5px] p-2">
                <div class = "w-full h-full bg-[#373B47] rounded-[5px]">  </div>
            </div>
        </div>
        
    );
    };

    export default CryptoPriceCard;
