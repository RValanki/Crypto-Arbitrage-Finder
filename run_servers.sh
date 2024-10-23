#!/bin/bash

# This script is used to start the frontend and backend servers
# Instructions:
# 1. Open terminal
# 2. cd to the root project directory "CRYPTO_ARBITRAGE_FINDER"
# 3. Run the script using the command "bash run_servers.sh"

# Get the directory of the script
DIR="$(cd "$(dirname "$0")" && pwd)"

# Function to start frontend server
echo "Starting frontend server..."
osascript -e 'tell application "Terminal" to do script "cd '$DIR'/frontend/crypto-arbitrage-finder && npm install && npm run start"'

# Function to start backend server
echo "Starting backend server..."
osascript -e 'tell application "Terminal" to do script "cd '$DIR'/backend/crypto_arbitrage_finder_backend && [ ! -d venv ] && python3 -m venv venv; source venv/bin/activate && pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate && python manage.py runserver"'

echo "Both servers are now running."
