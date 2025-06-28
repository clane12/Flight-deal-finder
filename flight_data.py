import os
from dotenv import load_dotenv
import requests

# load env file
load_dotenv()

# get token from env file
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')


class Flight_info():
    def __init__(self):
        self.url = "https://api.sheety.co/96e4daf37314c202a2aa6ae37c278eb1/flightDeal/sheet1"
        self.headers ={
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }
        self.responce = requests.get(url=self.url, headers=self.headers)

        self.content = self.responce.json()

        self.iatacodes = self.get_destination_codes()
        self.max_price = self.get_max_prices()
        self.city_name = self.get_city_names()


    #  get IATA codes as a list
    def get_destination_codes(self):
        codes = [item['iataCode'] for item in self.content['sheet1']]
        return codes


    #  get budget price as a list
    def get_max_prices(self):
        max_price = [item['lowestPrice'] for item in self.content['sheet1']]
        return max_price


    #  get city names as a list
    def get_city_names(self):
        city_names = [item['city'] for item in self.content['sheet1']]
        return city_names



    # get customers emails and names info.
    def get_email(self):
        URL = "https://api.sheety.co/96e4daf37314c202a2aa6ae37c278eb1/flightDeal/formResponses1"

        headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }

        responce = requests.get(url=URL, headers=headers)
        content = responce.json()

        emails = [item['email'] for item in content['formResponses1']]
        # print(emails)
        return emails

# he = Flight_info()