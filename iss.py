import requests
import datetime as dt
import smtplib

my_latitude =  19.240330
my_longitude =  73.130539
my_email = "dkhapekar8520@gmail.com"
password = "darshankhapekar"

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()["iss_position"]
    iss_longitude = float(data["longitude"])
    iss_latitude = float(data["latitude"])

    if my_latitude-5 <= iss_latitude <= my_latitude+5 and my_longitude-5 <= iss_longitude <= my_longitude+5:
        return True

def is_night():
    parameters = {
        "lat": 19.240330,
        "lng": 73.130539,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

if iss_overhead() and is_night():

    with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg="Subject:ISS is overhead\n\n "
            "Look Above the ISS is Over you")

