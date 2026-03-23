from tracker import get_iss_position
from user_input import get_user_position
from map_utils import create_map
from utils import calculate_distance, display_locations


def main():
    user_latitude, user_longitude = get_user_position()
    iss_latitude, iss_longitude = get_iss_position()

    user_position = (user_latitude, user_longitude)
    iss_position = (iss_latitude, iss_longitude)

    iss_user_distance_kilometer = calculate_distance(user_position, iss_position)

    display_locations(
        iss_latitude,
        iss_longitude,
        user_latitude,
        user_longitude,
        iss_user_distance_kilometer,
    )

    create_map(user_position, iss_position, iss_user_distance_kilometer)


if __name__ == "__main__":
    main()