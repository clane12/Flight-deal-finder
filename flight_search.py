from dotenv import load_dotenv
import os
import requests
import datetime

# load env file
load_dotenv()

# get the api key and secret from env
FLIGHT_APIKEY = os.getenv("AMADEUS_FLIGHT_APIKEY")
FLIGHT_APISECRET = os.getenv("AMADEUS_FLIGHT_APISECRET")


# create a class search flight
class Search_flight():
    def __init__(self):
        self.token = self.get_token() # this the token to access the flight api through oauth
        # self.get_data()
        self.date_today = datetime.datetime.now() + datetime.timedelta(days=2)
        self.date_today = str(self.date_today.strftime("%Y-%m-%d"))
        self.date = datetime.datetime.now()
        self.todate = self.date + datetime.timedelta(days=(6*30))
        self.todate = str(self.todate.strftime("%Y-%m-%d"))
        print(self.todate, self.date_today)


    # get the token for Oauth2.0, you need the token to access and get all the data.
    def get_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "grant_type": "client_credentials",
            "client_id": FLIGHT_APIKEY,
            "client_secret": FLIGHT_APISECRET,
        }

        responce = requests.post(url=url, headers=headers, data=data)
        content = responce.json()
        return content['access_token']



    # get IATA codes of all the city names that you want to visit.
    def city_search(self, cityname):
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        parameters = {
            "keyword": cityname,
            "max": 1
        }

        responce = requests.get(url=url, headers=headers, params=parameters)
        content = responce.json()
        return content



    # get flight data with prices and destinations
    def get_data(self, price, destination_code, is_direct):
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        parameters = {
            "originLocationCode": "YUL",
            "destinationLocationCode": destination_code,
            "departureDate": self.date_today,
            "returnDate": self.todate,
            "adults": 1,
            "maxPrice": price,
            "currencyCode": "CAD",
            "nonStop": f"{is_direct}",
            "max": 2
        }


        responce = requests.get(url=url, headers=headers, params=parameters)
        content = responce.json()
        return content

