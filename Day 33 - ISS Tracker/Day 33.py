cls = lambda: print("\033[2J\033[;H", end='')
cls()

import json
import requests
import datetime as dt
import time
"""
Day 33 - APIs
"""
HOME_LAT = 4.720520
HOME_LNG = -74.117610
iss_lat = 0
iss_lng = 0

def current_iss():
    global iss_lat
    global iss_lng
    # Creating a variable to store the response from the API
    response_ISS = requests.get(url=r"http://api.open-notify.org/iss-now.json")
    # Raising an exception for a failure in the API/Client
    response_ISS.raise_for_status()
    
    # Retrieving the data
    data_ISS = response_ISS.json()
    position = data_ISS["iss_position"]
    iss_lat = float(position["latitude"])
    iss_lng = float(position["longitude"])
    return position

parameters = {
    "lat": HOME_LAT,
    "lng": HOME_LNG,
    "formatted": 0,
}
response = requests.get(url=r"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

t = dt.datetime.now()
actual_time = int(str(t).split(":")[0].split(" ")[1])
sunrise = sunrise.split("T")[1].split(":")[0]
sunset = sunset.split("T")[1].split(":")[0]
adjusted_sunrise = int(sunrise)-5
adjusted_sunset = int(sunset)-4

run = True
while run:
    iss_position = current_iss()
    print(f"ISS current location is: {iss_position}")
    if actual_time > adjusted_sunrise and actual_time < adjusted_sunset:
        print("It is daytime, so ISS can't be seen")
    else:
        if iss_lat >= HOME_LAT-5 and iss_lat <= HOME_LAT+5 and iss_lng >= HOME_LNG-5 and iss_lng <= HOME_LNG+5:
            print("The ISS is currently viewable from your location!")
        else:
            print("ISS is not viewable from Colombia")
    time.sleep(5)
        