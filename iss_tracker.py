import folium
import requests
import webbrowser
from citycoordinates import city_coords

from geopy import distance


# Function to get ISS position utilizing the 'ISS Current Location' API
def get_iss_position():
    req = requests.get("http://api.open-notify.org/iss-now.json")
    req.raise_for_status()
    data = req.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude


# Function created to prompt the user for the city they live in. Incase the city
# is not listed, the program will prompt the user for the Longitude and Latitude of their position.
# I also provided a website where they can acquire their coordinates
def get_user_position():
    print(
        "Welcome to the ISS tracker! Let us begin by acquiring your coordinates.",
        "If you don't know your coordinates, please visit this website: https://www.latlong.net/ \n",
    )
    
    while True:
        try:
            user_state = input("Enter your state: ").title()
            user_city = input("Enter your city: ").title()

            if user_state in city_coords and user_city in city_coords[user_state]:
                user_latitude, user_longitude = city_coords[user_state][user_city]
                print(f"Coordinates for {user_city}, {user_state} found: Latitude: {user_latitude}, Longitude: {user_longitude}")
                return user_latitude, user_longitude
            else:
                print(
                    "The city or state typed may not be listed. If it's not listed, you'll need to manually enter your coordinates."
                )

            # Prompt the user to enter coordinates manually if city/state not in city_coords
            user_latitude = float(input("What is your latitude? \n"))
            user_longitude = float(input("What is your longitude? \n"))
            return user_latitude, user_longitude
        except ValueError:
            print("Invalid input. Please enter valid numerical values for both latitude and longitude.")



# 'main' function created
def main():
    # Creating variable to contain the user's and the iss' position
    user_position = user_latitude, user_longitude = get_user_position()
    iss_position = iss_latitude, iss_longitude = get_iss_position()

    iss_user_distance_kilometer = round(
        (distance.distance(user_position, iss_position).km), 2
    )

    # Printing all of the information in the variables above
    print(
        f"The ISS is currently located over Latitude: {iss_latitude} and Longitude: {iss_longitude}\n"
    )

    print(
        f"Your position is: Latitude: {user_latitude} and Longitude: {user_longitude}\n"
    )

    print(
        f"The distance between you and the ISS's hover position is {iss_user_distance_kilometer} KM."
    )
    # Creating the map
    m = folium.Map(location=user_position, control_scale=False, zoom_start=3)

    # Adding the ISS' position marker to the map
    folium.Marker(
        location=(iss_position),
        tooltip="Click me!",
        popup=f"ISS Station Location (Latitude: {iss_latitude}, Longitude:{iss_longitude})",
        icon=folium.Icon(color="red"),
    ).add_to(m)

    # Adding the user's position marker to the map
    folium.Marker(
        location=(user_position),
        tooltip="Click me!",
        popup=f"Your Location (Latitude: {user_latitude}, Longitude:{user_longitude})",
        icon=folium.Icon(color="blue"),
    ).add_to(m)

    # Creating a line between both positions
    folium.PolyLine(
        locations=((user_position), (iss_position)),
        color="green",
        weight=6,
        popup=f"The distance between the ISS and your position is {iss_user_distance_kilometer} KM.",
    ).add_to(m)

    # Html file needs to be created and also will be opened once
    # the program is ran
    m.save("iss_location.html")
    webbrowser.open("iss_location.html")


# 'main' function called
main()
