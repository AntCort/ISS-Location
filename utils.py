from geopy import distance


def calculate_distance(user_position, iss_position):
    # Returnns the distance between the user and the ISS.
    return round(distance.distance(user_position, iss_position).km, 2)


def display_locations(
    iss_latitude,
    iss_longitude,
    user_latitude,
    user_longitude,
    distance_km,
):
    print("\nISS location:")
    print(f"Latitude: {iss_latitude}")
    print(f"Longitude: {iss_longitude}")

    print("\nYour location:")
    print(f"Latitude: {user_latitude}")
    print(f"Longitude: {user_longitude}")

    print(f"\nDistance between you and the ISS: {distance_km} KM")
