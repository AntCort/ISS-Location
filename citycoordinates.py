import csv

# Creating a dictionary to contain cities from around the world and their coordinates
# to help get the users coordinates
city_coords = {}

file = "uscities.csv"
with open(file, "r", newline="", encoding="utf-8") as data:
    reader = csv.reader(data)
    next(reader)

    for row in reader:
        state = row[0]
        city = row[1]
        lat = float(row[2])
        long = float(row[3])
        
        if state not in city_coords:
            city_coords[state] = {}
        
        city_coords[state][city] = (lat, long)
