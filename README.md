# ISS Location Map

This program generates an interactive map displaying the current location of the International Space Station (ISS) and a user's specified location. The map is created using Folium, a Python library for interactive mapping. I added the html file that is generated once the program has been run. The program also prompts the user to enter their coordinates to show the distance between the station and their location. The prompt includes a website where they can acquire their exact coordinates.

## Prerequisites

Before running the program, ensure you have the following dependencies installed:

- Python
- Folium library
- Requests library
- Webbrowser library
- Geopy library

To install the required dependencies, you can use the following command:

```bash
pip install -r requirements.txt
```

## How to run

- git clone https://github.com/your-username/iss-location-map.git
- cd iss-location-map
- pip install -r requirements.txt
- python iss_tracker.py


## Bugs and Future Plans

- Fix Duplicate City Names: Currently, the program does not handle multiple cities with the same name. I plan to fix this by including the state in the city lookup to ensure accurate identification.
- User Choice for Coordinates Input: I will add a feature allowing users to choose whether they want to enter their coordinates directly or specify their city and state.



