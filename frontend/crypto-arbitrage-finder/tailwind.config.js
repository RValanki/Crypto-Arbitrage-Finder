// tailwind.config.js
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}", // Ensure Tailwind scans your files
  ],
  theme: {
    extend: {
      colors: {
        'background-gray': '#181A1F', // Add your custom color here
      },
      animation: {
        fadeIn: 'fadeIn 1s ease-in-out forwards',
        fadeInFast:  'fadeIn 0.7s ease-in-out forwards',// Animation for fade-in effect
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
      },
    },
  },
  plugins: [],
};
