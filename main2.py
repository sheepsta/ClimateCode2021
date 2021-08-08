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
from guizero import *
import datetime
from datetime import date, datetime


app = App(title = "Sprare", width = "1200", height = "700")
name = Text(app, text = "Sprare", size = 50, align = "top", color = "#FFFFFF")

#amount of locations selected
locationNumbers = Text(app, text = "\nHow many locations would like you like to investigate?")

Numbers = Combo(app,
                   options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                   selected = "number", width = 20)

Numbers.bg = "white"

figure(figsize=(8, 6), dpi=80)

inputted_locations = []

def textbox(): #adds new textboxes depending on the number selected
    if Numbers.value == "1":
        location1 = TextBox(app, text = "Input first location:")
        inputted_locations.append(location1.value)
        
    elif Numbers.value == "2":
        location1 = TextBox(app, text = "Input first location:")
        location2 = TextBox(app, text = "Input second location:")
        inputted_locations.append(location1.value)
        inputted_locations.append(location2.value)


    elif Numbers.value == "3":
        location1 = TextBox(app, text = "Input first location:")
        location2 = TextBox(app, text = "Input second location:")
        location3 = TextBox(app, text = "Input third location:")
        inputted_locations.append(location1.value)
        inputted_locations.append(location2.value)
        inputted_locations.append(location3.value)

    elif Numbers.value == "4":
        location1 = TextBox(app, text = "Input first location:")
        location2 = TextBox(app, text = "Input second location:")
        location3 = TextBox(app, text = "Input third location:")
        location4 = TextBox(app, text = "Input fourth location:")
        inputted_locations.append(location1.value)
        inputted_locations.append(location2.value)
        inputted_locations.append(location3.value)
        inputted_locations.append(location4.value)
        
    elif Numbers.value == "5":
        location1 = TextBox(app, text = "Input first location:")
        location2 = TextBox(app, text = "Input second location:")
        location3 = TextBox(app, text = "Input third location:")
        location4 = TextBox(app, text = "Input fourth location:")
        location5 = TextBox(app, text = "Input fifth location:")
        inputted_locations.append(location1.value)
        inputted_locations.append(location2.value)
        inputted_locations.append(location3.value)
        inputted_locations.append(location4.value)
        inputted_locations.append(location5.value)
        
    elif Numbers.value == "6":
        location1 = TextBox(app, text = "Input first location:")
        location2 = TextBox(app, text = "Input second location:")
        location3 = TextBox(app, text = "Input third location:")
        location4 = TextBox(app, text = "Input fourth location:")
        location5 = TextBox(app, text = "Input fifth location:")
        location6 = TextBox(app, text = "Input sixth location:")
        inputted_locations.append(location1.value)
        inputted_locations.append(location2.value)
        inputted_locations.append(location3.value)
        inputted_locations.append(location4.value)
        inputted_locations.append(location5.value)
        inputted_locations.append(location6.value)
        
    elif Numbers.value == "7":
        location1 = TextBox(app, text = "Input first location:")
        location2 = TextBox(app, text = "Input second location:")
        location3 = TextBox(app, text = "Input third location:")
        location4 = TextBox(app, text = "Input fourth location:")
        location5 = TextBox(app, text = "Input fifth location:")
        location6 = TextBox(app, text = "Input sixth location:")
        location7 = TextBox(app, text = "Input seventh location:")
        inputted_locations.append(location1.value)
        inputted_locations.append(location2.value)
        inputted_locations.append(location3.value)
        inputted_locations.append(location4.value)
        inputted_locations.append(location5.value)
        inputted_locations.append(location6.value)
        inputted_locations.append(location7.value)
        
    elif Numbers.value == "8":
        location1 = TextBox(app, text = "Input first location:")
        location2 = TextBox(app, text = "Input second location:")
        location3 = TextBox(app, text = "Input third location:")
        location4 = TextBox(app, text = "Input fourth location:")
        location5 = TextBox(app, text = "Input fifth location:")
        location6 = TextBox(app, text = "Input sixth location:")
        location7 = TextBox(app, text = "Input seventh location:")
        location8 = TextBox(app, text = "Input eigth location:")
        inputted_locations.append(location1.value)
        inputted_locations.append(location2.value)
        inputted_locations.append(location3.value)
        inputted_locations.append(location4.value)
        inputted_locations.append(location5.value)
        inputted_locations.append(location6.value)
        inputted_locations.append(location7.value)
        inputted_locations.append(location8.value)
        
    elif Numbers.value == "9":
        location1 = TextBox(app, text = "Input first location:")
        location2 = TextBox(app, text = "Input second location:")
        location3 = TextBox(app, text = "Input third location:")
        location4 = TextBox(app, text = "Input fourth location:")
        location5 = TextBox(app, text = "Input fifth location:")
        location6 = TextBox(app, text = "Input sixth location:")
        location7 = TextBox(app, text = "Input seventh location:")
        location8 = TextBox(app, text = "Input eigth location:")
        location9 = TextBox(app, text = "Input ninth location:")
        inputted_locations.append(location1.value)
        inputted_locations.append(location2.value)
        inputted_locations.append(location3.value)
        inputted_locations.append(location4.value)
        inputted_locations.append(location5.value)
        inputted_locations.append(location6.value)
        inputted_locations.append(location7.value)
        inputted_locations.append(location8.value)
        inputted_locations.append(location9.value)
        
    elif Numbers.value == "10":
        location1 = TextBox(app, text = "Input first location:")
        location2 = TextBox(app, text = "Input second location:")
        location3 = TextBox(app, text = "Input third location:")
        location4 = TextBox(app, text = "Input fourth location:")
        location5 = TextBox(app, text = "Input fifth location:")
        location6 = TextBox(app, text = "Input sixth location:")
        location7 = TextBox(app, text = "Input seventh location:")
        location8 = TextBox(app, text = "Input eigth location:")
        location9 = TextBox(app, text = "Input ninth location:")
        location10 = TextBox(app, text = "Input tenth location:")
        inputted_locations.append(location1.value)
        inputted_locations.append(location1.value)
        inputted_locations.append(location2.value)
        inputted_locations.append(location3.value)
        inputted_locations.append(location4.value)
        inputted_locations.append(location5.value)
        inputted_locations.append(location6.value)
        inputted_locations.append(location7.value)
        inputted_locations.append(location8.value)
        inputted_locations.append(location9.value)
        inputted_locations.append(location10.value)

submit_btn = PushButton(app, text = "Bring Textboxes", command = textbox) #press to activate new textboxes
submit_btn.bg = "green"

startingdate = Text(app, text = "Starting Date")

day1 = Combo(app,
            options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14","15",
                       "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29","30", "31"],
            selected = "1", width = 10)
day1.bg = "white"



month1 = Combo(app,
            options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
            selected = "1", width = 10)
month1.bg = "white"

year1 = TextBox(app, text = "2021", width = "20", height = "87")
year1.bg = "white"

finishingdate = Text(app, text = "Finishing Date")

day2 = Combo(app,
            options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14","15",
                       "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29","30", "31"],
            selected = "1", width = 10)
day2.bg = "white"

month2 = Combo(app,
            options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
            selected = "1", width = 10)
month2.bg = "white"

year2 = TextBox(app, text = "2021", width = "20", height = "87")
year2.bg = "white"

points = []

def plot_show():
  for city in inputted_locations:
      print(city)
  city_index = inputted_locations.index(input("Which of the above locations did you want to view a graph for?"))
  data_array[city_index].plot(y=['tavg', 'tmin', 'tmax'])
  plt.show()

#adding locations to locations array
##while True:
##  location_input_confirm = input("Add another location?").lower()
##  if location_input_confirm == "yes":
##    location_input = input("Input location: ")
##    inputted_locations.append(location_input)
##  else:
##    print("Locations have been compiled succesfully")
##    break

def submit():
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

    #fetching date range
    returned_starting_date = datetime(int(year1.value), int(month1.value), int(day1.value))
    returned_ending_date = datetime(int(year2.value), int(month2.value), int(day2.value))

    i = 0
    #adding data to array to be annalyzed
    data_array = []
    for point in points:
      current_city = inputted_locations[i]
      i += 1
      data = Monthly(point, returned_starting_date, returned_ending_date)
      data = data.fetch()
##      if len(data) > 0:
##        print(f"Weather data for {current_city} fetched succesfully.")
      data_array.append(data)
      
    alg_results = weather_algorithm(data_array, inputted_locations)

    if Numbers.value == "1":
        text = Text(app, text = "1")
        text = Text(app, text = alg_results[1])
        btn = PushButton(app, text = "See graph", command = plot_show)
        
##      if int(alg_results[i]) <= 42: bring back at the end when everything works allocates colors to how big the number is
##          text.text_color = "red"
##    elif int(alg_results[i]) >= 60:
##        text.text_color = "yellow"
##    elif int(alg_results[i]) >= 75:
##        text.text_color = "green"
    
    elif Numbers.value == "2":
        text = Text(app, text = "1")
        text = Text(app, text = alg_results[1])
        text = Text(app, text = "2")
        text = Text(app, text = alg_results[2])
        btn = PushButton(app, text = "See graph", command = plot_show)
   

    
    elif Numbers.value == "3":
        text = Text(app, text = "1")
        text = Text(app, text = alg_results[1])
        text = Text(app, text = "2")
        text = Text(app, text = alg_results[2])
        text = Text(app, text = "3")
        btn = PushButton(app, text = "See graph", command = plot_show)
   

        
    elif Numbers.value == "4":
        text = Text(app, text = "1")
        text = Text(app, text = alg_results[1])
        text = Text(app, text = "2")
        text = Text(app, text = alg_results[2])
        text = Text(app, text = "3")
        text = Text(app, text = alg_results[3])
        text = Text(app, text = "4")
        text = Text(app, text = alg_results[4])
        btn = PushButton(app, text = "See graph", command = plot_show)
   

        
    elif Numbers.value == "5":
        text = Text(app, text = "1")
        text = Text(app, text = alg_results[1])
        text = Text(app, text = "2")
        text = Text(app, text = alg_results[2])
        text = Text(app, text = "3")
        text = Text(app, text = alg_results[3])
        text = Text(app, text = "4")
        text = Text(app, text = alg_results[4])
        text = Text(app, text = "5")
        text = Text(app, text = alg_results[5])
        btn = PushButton(app, text = "See graph", command = plot_show)
   

        
    elif Numbers.value == "6":
        text = Text(app, text = "1")
        text = Text(app, text = alg_results[1])
        text = Text(app, text = "2")
        text = Text(app, text = alg_results[2])
        text = Text(app, text = "3")
        text = Text(app, text = alg_results[3])
        text = Text(app, text = "4")
        text = Text(app, text = alg_results[4])
        text = Text(app, text = "5")
        text = Text(app, text = alg_results[5])
        text = Text(app, text = "6")
        text = Text(app, text = alg_results[6])
        btn = PushButton(app, text = "See graph", command = plot_show)
   

        
    elif Numbers.value == "7":
        text = Text(app, text = "1")
        text = Text(app, text = alg_results[1])
        text = Text(app, text = "2")
        text = Text(app, text = alg_results[2])
        text = Text(app, text = "3")
        text = Text(app, text = alg_results[3])
        text = Text(app, text = "4")
        text = Text(app, text = alg_results[4])
        text = Text(app, text = "5")
        text = Text(app, text = alg_results[5])
        text = Text(app, text = "6")
        text = Text(app, text = alg_results[6])
        text = Text(app, text = "7")
        text = Text(app, text = alg_results[7])
        btn = PushButton(app, text = "See graph", command = plot_show)
   

    elif Numbers.value == "8":
        text = Text(app, text = "1")
        text = Text(app, text = alg_results[1])
        text = Text(app, text = "2")
        text = Text(app, text = alg_results[2])
        text = Text(app, text = "3")
        text = Text(app, text = alg_results[3])
        text = Text(app, text = "4")
        text = Text(app, text = alg_results[4])
        text = Text(app, text = "5")
        text = Text(app, text = alg_results[5])
        text = Text(app, text = "6")
        text = Text(app, text = alg_results[6])
        text = Text(app, text = "7")
        text = Text(app, text = alg_results[7])
        text = Text(app, text = "8")
        text = Text(app, text = alg_results[8])
        btn = PushButton(app, text = "See graph", command = plot_show)
   

        
    elif Numbers.value == "9":
        text = Text(app, text = "1")
        text = Text(app, text = alg_results[1])
        text = Text(app, text = "2")
        text = Text(app, text = alg_results[2])
        text = Text(app, text = "3")
        text = Text(app, text = alg_results[3])
        text = Text(app, text = "4")
        text = Text(app, text = alg_results[4])
        text = Text(app, text = "5")
        text = Text(app, text = alg_results[5])
        text = Text(app, text = "6")
        text = Text(app, text = alg_results[6])
        text = Text(app, text = "7")
        text = Text(app, text = alg_results[7])
        text = Text(app, text = "8")
        text = Text(app, text = alg_results[8])
        text = Text(app, text = "9")
        text = Text(app, text = alg_results[9])
        btn = PushButton(app, text = "See graph", command = plot_show)
   
        
    elif Numbers.value == "10":
        text = Text(app, text = "1")
        text = Text(app, text = alg_results[1])
        text = Text(app, text = "2")
        text = Text(app, text = alg_results[2])
        text = Text(app, text = "3")
        text = Text(app, text = alg_results[3])
        text = Text(app, text = "4")
        text = Text(app, text = alg_results[4])
        text = Text(app, text = "5")
        text = Text(app, text = alg_results[5])
        text = Text(app, text = "6")
        text = Text(app, text = alg_results[6])
        text = Text(app, text = "7")
        text = Text(app, text = alg_results[7])
        text = Text(app, text = "8")
        text = Text(app, text = alg_results[8])
        text = Text(app, text = "9")
        text = Text(app, text = alg_results[9])
        text = Text(app, text = "10")
        text = Text(app, text = alg_results[10])
        btn = PushButton(app, text = "See graph", command = plot_show)
   
    
submit_btn = PushButton(app, text = "Submit", command = submit)
submit_btn.bg = "green"


##print("Enter the starting and ending dates for the data. ")
##print("Calculating score for locations. This may take a few minutes...")


##print("Plotting data...")
# Plot line chart including average, minimum and maximum temperature



##while True:
##  if input("Would you like to a view a temperature graph for your locations?") == "yes":
##    plot_show()
##  else:
##    break
##print("All operations completed")

