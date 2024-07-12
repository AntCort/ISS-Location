import csv

# Creating a dictionary to contain cities from around the world and their coordinates
# to help get the users coordinates
city_coords = {}

file = "worldcities.csv"
with open(file, "r", newline="", encoding="utf-8") as data:
    reader = csv.reader(data)
    next(reader)  # Skip header row if exists

    for row in reader:
        city = row[0]  # First column is city
        lat = float(row[1])  # Second column is latitude
        long = float(row[2])  # Third column is longitude
        city_coords[city] = (lat, long)
