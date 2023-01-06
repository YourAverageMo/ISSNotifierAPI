from datetime import datetime
from tkinter import *

import requests

MY_LAT = 61.507351
MY_LNG = -0.127758


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(
        url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    sun_data = response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    hour_now = datetime.now().hour

    if sunrise >= hour_now >= sunset:
        return True


def is_iss_overhead():
    response = requests.get(
        url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_pos = response.json()
    iss_lat = float(iss_pos["iss_position"]["latitude"])
    iss_lng = float(iss_pos["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_lat <= MY_LAT + 5 and MY_LNG-5 <= iss_lng <= MY_LNG+5:
        return True


# below this is the part u put into a while loop using time.sleep(60) so the program keeps running once every min. im not doing that for obvious reasons.
if is_iss_overhead() and is_night():
    # insert email code here. im not doing it cuz of the reasons stated in previous project
    pass
