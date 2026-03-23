import requests


API_URL = "http://api.open-notify.org/iss-now.json"


def get_iss_position():
    # Get the current ISS latitude and longitude.
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()

    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return iss_latitude, iss_longitude