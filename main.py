import requests
import urllib.parse
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily, Stations, Monthly
import json
import urllib
from elevation import elevation
from location import location
from datefunc import starting_date_func
from datefunc import ending_date_func
import base64
from io import BytesIO
from algorithm import weather_algorithm
import math
from matplotlib.pyplot import figure

figure(figsize=(8, 6), dpi=80)

inputted_locations = []

inputted_locations.append(input("Input first location: "))

#adding locations to locations array
while True:
  location_input_confirm = input("Add another location?").lower()
  if location_input_confirm == "yes":
    location_input = input("Input location: ")
    inputted_locations.append(location_input)
  else:
    print("Locations have been compiled succesfully")
    break

points = []

#fetching lattitude, longitude, and elevation to get weather data
for place in inputted_locations:
  # for place in inputted_locations: 
    #returns the lat and lng for the inputted location
  location_input = location(place)
  lattitude = location_input[0]
  longitude = location_input[1]
    #returns the elevation for the lat lng values
  elevation_output = elevation(lattitude, longitude)
  inputted_location = Point(lattitude, longitude, elevation_output)
  points.append(inputted_location)

print("Enter the starting and ending dates for the data. ")

#fetching date range
returned_starting_date = starting_date_func()
returned_ending_date = ending_date_func()

i = 0
#adding data to array to be annalyzed
data_array = []
for point in points:
  current_city = inputted_locations[i]
  i += 1
  data = Monthly(point, returned_starting_date, returned_ending_date)
  data = data.fetch()
  if len(data) > 0:
    print(f"Weather data for {current_city} fetched succesfully.")
  data_array.append(data)

print("Calculating score for locations. This may take a few minutes...")

alg_results = weather_algorithm(data_array, inputted_locations)

for i in alg_results:
  print(f"Analysis for {i}")
  print(f"Total score: {alg_results[i][0]} / 100")
  if alg_results[i][0] > 90.0:
    print("This is a near perfect score.")
  elif alg_results[i][0] > 80.0:
    print("This is a very good score")
  elif alg_results[i][0] > 70.0:
    print("This is a good score.")
  elif alg_results[i][0] > 60.0:
    print("This is an okay score.")
  elif alg_results[i][0] > 50.0:
    print("This is an adequate score.")
  elif alg_results[i][0] > 40.0:
    print("This is not a good score.")
  elif alg_results[i][0] < 40.0:
    print("This is a bad score.")
  print(f"Temperature score for {i} is {alg_results[i][2]} / 50")
  print(f"Preciptation score for {i} is {alg_results[i][1]} / 30")
  print(f"Sea level air pressure score for {i} is {alg_results[i][4]} / 15")
  print(f"Wind score for {i} is {alg_results[i][3]} / 5")

  

print("Plotting data...")
# Plot line chart including average, minimum and maximum temperature

def plot_show():
  for city in inputted_locations:
      print(city)
  city_index = inputted_locations.index(input("Which of the above locations did you want to view a graph for?"))
  data_array[city_index].plot(y=['tavg', 'tmin', 'tmax'])
  plt.show()

while True:
  if input("Would you like to a view a temperature graph for your locations?") == "yes":
    plot_show()
  else:
    break
print("All operations completed")












