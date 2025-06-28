✈️ Flight Deal Finder & Notification System
A Flight Deal Finder application that searches for cheap flight offers based on a user's preferred destinations and budget. It integrates with multiple APIs to fetch flight details, sends notifications via SMS and email, and updates flight information on a spreadsheet.

✨ Features
🌍 Retrieves IATA codes for cities from a Google Sheet.

💸 Searches for flights based on predefined budget and destination criteria.

🛫 Filters flights by price and direct flight preference.

📩 Sends email and SMS notifications to users about flight deals.

📊 Updates the Google Sheet with IATA codes for cities.

📦 Requirements
Python 3.x+

requests: To fetch flight data and communicate with APIs.

dotenv: To securely load environment variables from a .env file.

twilio: For sending SMS notifications via Twilio.

smtplib: For sending email notifications via SMTP.

Google Sheets API: To interact with Google Sheets for storing flight data.

🛠 Setup
Clone or download the project.

Install the required dependencies:

bash
Copy
Edit
pip install requests twilio python-dotenv
Create a .env file to securely store sensitive credentials:

MY_EMAIL="your_email@example.com"
PASSWORD="your_email_password"
TWILIO_PHONE_NUMBER="your_twilio_phone_number"
TWILIO_SID="your_twilio_sid"
TWILIO_TOKEN="your_twilio_token"
FLIGHT_APIKEY="your_amadeus_api_key"
FLIGHT_APISECRET="your_amadeus_api_secret"
SHEETY_TOKEN="your_sheety_token"
Run the script:

python flight_deals.py
🎮 How It Works
Retrieve City Data: The application fetches a list of cities and their corresponding IATA codes from a Google Sheet via the Sheety API.

Flight Search: Using the Amadeus API, it searches for flights based on the IATA codes and user-defined price limits, filtering for direct flights.

Email & SMS Notifications: When a flight offer is found, notifications are sent to users via email and SMS using smtplib and Twilio.

Update Google Sheets: The IATA codes of cities are updated back to the Google Sheet for further use.

🚀 How to Use
Set your email and password for email notifications, and Twilio credentials for SMS notifications in the .env file.

Set your Amadeus API credentials to retrieve flight data and Sheety token for Google Sheets interaction.

Run the script, which will search for flight deals, notify users, and update the Google Sheet with relevant information.

🧩 Future Enhancements
🎨 User Interface: Add a front-end interface to let users interactively set their preferences and receive real-time updates.

🔄 Multiple API Integrations: Integrate additional flight providers for a broader range of flight data.

📅 Custom Date Ranges: Allow users to specify custom travel dates.

🚀 Notification Preferences: Let users choose their preferred notification method (SMS, email, or both).

