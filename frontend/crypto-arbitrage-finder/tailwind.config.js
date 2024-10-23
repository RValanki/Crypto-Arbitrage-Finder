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
    },
  },
  plugins: [],
};
