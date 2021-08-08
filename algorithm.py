#algorithm to give locations a score out of 100

from math import isnan

def weather_algorithm(data_array, inputted_locations):
  final_scores = {}

  location_index = 0

  total_score = 0.0

  total_avg_temp = 0.0
  total_avg_pressure = 0.0
  total_avg_wind = 0.0
  total_avg_prcp = 0.0

  temp_score = 55.0
  pressure_score = 10.0
  wind_score = 5.0
  prcp_score = 30.0

  i = 0.0

  for key in data_array:
    if len(key["tavg"]) > 0:
      for temperature in key["tavg"]:
        if isnan(float(temperature)) == False:
          temperature = float(temperature)
          total_avg_temp += temperature
          i += 1.0
      final_avg_temp = float(total_avg_temp) / float(i)

      for temperature in key["tmin"]:
        if temperature < -3.8:
          temp_score -= 3.0
          break
        elif temperature < 5.0:
          temp_score -= 1.5
          break
      
      for temperature in key["tmax"]:
        if temperature > 50:
          temp_score -= 20
          break
        elif temperature > 45:
          temp_score -= 5
          break
      
      if final_avg_temp > 18.0:
        while final_avg_temp > 18.0:
          temp_score -= 2.5
          final_avg_temp -= 1.0
      elif final_avg_temp < 18.0:
        while final_avg_temp < 18.0:
          temp_score -= 0.8
          final_avg_temp += 1.0

      i = 0.0
      for pressure in key["pres"]:
        if isnan(float(pressure)) == False:
          pressure = float(pressure)
          total_avg_pressure += pressure
          i += 1.0
      total_avg_pressure = float(total_avg_pressure) / float(i)

      if total_avg_pressure > 1013.25:
        while total_avg_pressure > 1013.25:
          pressure_score -= 1.0
          total_avg_pressure -= 1.0
      elif total_avg_pressure < 1013.25:
        while total_avg_pressure < 1013.25:
          pressure_score -= 1.0
          total_avg_pressure += 1.0
      
      i = 0.0  
      for wind in key["wspd"]:
        if isnan(float(wind)) == False:
          wind = float(wind)
          total_avg_wind += wind
          i += 1.0
      total_avg_wind = float(total_avg_wind) / float(i)

      if total_avg_wind > 25.0:
        wind_score = 2.0
      elif total_avg_wind > 15.0:
        wind_score = 3.5
      elif total_avg_wind > 5.0:
        wind_score = 5.0
      else:
        wind_score = 4.0

      i = 0.0
      for prcp in key["prcp"]:
        if isnan(float(prcp)) == False:
          prcp = float(prcp)
          total_avg_prcp += prcp
          i += 1.0
      total_avg_prcp = float(total_avg_prcp) / float(i)

      if total_avg_prcp < 30.0:
        prcp_score = 3.0
      elif total_avg_prcp < 50.0:
        prcp_score = 8.0
      elif total_avg_prcp < 80.0:
        prcp_score = 12.0
      elif total_avg_prcp < 110.0:
        prcp_score = 17.0
      elif total_avg_prcp < 140.0:
        prcp_score = 22.0
      elif total_avg_prcp < 180.0:
        prcp_score = 25.0
      else:
        prcp_score = 30.0

      total_score = prcp_score + temp_score + pressure_score + wind_score

      location_scores = []
      location_scores.append(total_score)
      location_scores.append(prcp_score)
      location_scores.append(temp_score)
      location_scores.append(wind_score)
      location_scores.append(pressure_score)

      final_scores[inputted_locations[location_index]] = location_scores

      total_score = 0.0

      total_avg_temp = 0.0
      total_avg_pressure = 0.0
      total_avg_wind = 0.0
      total_avg_prcp = 0.0

      temp_score = 50.0
      pressure_score = 15.0
      wind_score = 5.0
      prcp_score = 30.0

      i = 0.0

      location_index += 1
    else:
      print("Unable to fetch weather data for given location. Please try another location")

  return final_scores



    
  

  


    
    
