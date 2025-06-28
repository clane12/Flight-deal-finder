import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

# load env file
load_dotenv()


# load API data from .env file
PHONE_NUM = os.getenv("TWILIO_PHONE_NUMBER")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
MY_NUMBER = "+14387731635"


class Messages:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    # send a message
    def send_message(self, price, city, code, going_date, coming_date):
        message = self.client.messages.create(
            body=f"Only {price} to fly from Montreal-YUL to {city}-{code}, from {going_date} to {coming_date}",
            from_=PHONE_NUM,
            to=MY_NUMBER
        )
