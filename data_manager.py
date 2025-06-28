import os
import requests
from dotenv import load_dotenv

# load env file
load_dotenv()

# get the token from env file
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')


# create a class sheety details
class Sheety_details():
    def __init__(self):
        self.geturl = "https://api.sheety.co/96e4daf37314c202a2aa6ae37c278eb1/flightDeal/sheet1"
        self.posturl = "https://api.sheety.co/96e4daf37314c202a2aa6ae37c278eb1/flightDeal/sheet1"
        self.city_names = self.get_city_names(self.geturl)



# get the names of all the cities that are in the spreadsheet.
    def get_city_names(self, url):
        headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }

        responce = requests.get(url=url, headers=headers)
        content = responce.json()
        city_names = [item['city'] for item in content['sheet1']]
        return city_names



# created to insert the iata codes into the spreadsheet based on the cities.
    def put_iatacode(self, code, city, objectid: int):
        url = f"https://api.sheety.co/96e4daf37314c202a2aa6ae37c278eb1/flightDeal/sheet1"

        parameters = {
            "sheet1":{
            "city": city,
            "iataCode": code,
        }}

        headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }

        responce = requests.put(url=f"{url}/{objectid}", json=parameters, headers=headers)
        content = responce.text
        print(content)





# sheety = Sheety_details()