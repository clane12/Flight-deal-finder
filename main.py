# load the classes
import os
from dotenv import load_dotenv

from flight_search import Search_flight
from data_manager import Sheety_details
from flight_data import Flight_info
from notification_manager import Messages
import smtplib
load_dotenv()


# set the variable for the classes loaded from other files
# sheety_details = Sheety_details()
flight_search = Search_flight()
flights_data = Flight_info()

send_msg = Messages()

#-----------------------------------------------------------------------------------------------------------------#

"""get the names of cities from spreadsheet, then with the help of flight api get the IATA codes of the cities
   and then insert those codes into the spreadsheet"""
# this is a list of all the names of the cities that are in the spreadsheet.
# cities = sheety_details.city_names
#
#
# # so the spreadsheet starts with 1 and we want to add the iata files from id 2.
# start = 2
#
# # loop through the cities list and get the city name and code and add the codes into the spreadsheet.
# for item in cities:
#     details = flight_search.city_search(item) # get the details of the city including their IATA codes
#     city = details['data'][0]['name']
#     iata_code = details['data'][0]['iataCode']
#     # call the method put_iatacode created in the data manager and add the codes into it.
#     sheety_details.put_iatacode(code=iata_code, city=city, objectid=start)
#     start += 1


#-------------------------------------------------------------------------------------------------------------#
"""Get the hold of all the email to mail then about the offers, and setup the SMTP email. """

emails = flights_data.get_email()

my_email = os.getenv('MY_EMAIL')
password = os.getenv('PASSWORD')

def send_email(price, city, code, going_date, coming_date):
    send_email = smtplib.SMTP('smtp.gmail.com')
    send_email.starttls()
    send_email.login(user=my_email, password=password)
    message = f"Subject: offer alert \n\n Only CAD:{price} to fly from Montreal-YUL to {city}-{code}, from {going_date} to {coming_date}"
    for mail in emails:
        send_email.sendmail(
            from_addr=my_email,
            to_addrs=mail,
            msg=f"subject:offer alert\n\n {message}")
    send_email.close()




#---------------------------------------------------------------------------------------------------------------#


"""now here get the info of all the places you want to visit according to you set budget and prices"""

iatacodes = flights_data.iatacodes
prices = flights_data.max_price
city_names = flights_data.city_name

# go through the IATA codes and send the messages and emails to the users.
for i in range(len(iatacodes)):
    ticket_data = flight_search.get_data(destination_code=iatacodes[i], price=prices[i], is_direct="true")
    # if the count is equal to 0 that means there are no offers so next it will check for flights with stops.
    if ticket_data['meta']['count'] == 0:
        ticket_data = flight_search.get_data(destination_code=iatacodes[i], price=prices[i], is_direct="false")
        # if there are flights with stops then it will send a message and email to clients, else move forward.
        if ticket_data['meta']['count'] > 0:
            first_flight = ticket_data['data'][0]
            lowest_price = float(first_flight["price"]["grandTotal"])
            origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = first_flight["itineraries"][0]["segments"][1]["arrival"]["iataCode"]
            out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

            send_msg.send_message(price=lowest_price, code=destination, city=city_names[i], going_date=out_date,
                                  coming_date=return_date)
            send_email(price=lowest_price, code=destination, city=city_names[i], going_date=out_date,
                                  coming_date=return_date)

        print(ticket_data)
        # if it finds for direct flight then it will send a message to clients about the offers.
    elif ticket_data['meta']['count'] > 0:
        print(ticket_data)

        first_flight = ticket_data['data'][0]
        lowest_price = float(first_flight["price"]["grandTotal"])
        origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

        send_msg.send_message(price=lowest_price, code=destination, city= city_names[i],going_date=out_date, coming_date=return_date)

        send_email(price=lowest_price, code=destination, city=city_names[i], going_date=out_date,
                   coming_date=return_date)
