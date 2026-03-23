import requests


def get_user_position():
    # Get user's approximate location using IP.
    response = requests.get("http://ip-api.com/json/", timeout=10)
    response.raise_for_status()

    data = response.json()

    user_latitude = data["lat"]
    user_longitude = data["lon"]
    city = data.get("city", "Unknown")

    print(f"Detected your location: {city}")

    return user_latitude, user_longitude
