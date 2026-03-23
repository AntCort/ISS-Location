import folium
import webbrowser


OUTPUT_FILE = "iss_location.html"


def create_map(user_position, iss_position, distance_km):
    # Create and open the map with the location of the ISS
    # and the user.  
    
    user_latitude, user_longitude = user_position
    iss_latitude, iss_longitude = iss_position

    iss_map = folium.Map(location=user_position, zoom_start=3)

    folium.Marker(
        location=iss_position,
        popup=f"ISS Location\nLatitude: {iss_latitude}, Longitude: {iss_longitude}",
        icon=folium.Icon(color="red"),
    ).add_to(iss_map)

    folium.Marker(
        location=user_position,
        popup=f"Your Location\nLatitude: {user_latitude}, Longitude: {user_longitude}",
        icon=folium.Icon(color="blue"),
    ).add_to(iss_map)

    folium.PolyLine(
        locations=[user_position, iss_position],
        color="green",
        weight=4,
        popup=f"Distance: {distance_km} KM",
    ).add_to(iss_map)

    iss_map.save(OUTPUT_FILE)
    webbrowser.open(OUTPUT_FILE)