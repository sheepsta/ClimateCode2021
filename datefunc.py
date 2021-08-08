import datetime
from datetime import date, datetime

def starting_date_func():
  year = int(input("Enter the starting year: "))
  if year > 2021:
    print("Invalid starting year input.")
    return
  if input("Would you like to input a specific date? \nIf not, then the 1st of January will be automatically be used.") == "yes":
    month = int(input("Input the month:"))
    day = int(input("Input the day: "))
    start = datetime(year, month, day)
    print(f"This date was succesfully inputted: {start}")
  else:
    start = datetime(year, 1, 1)
    print(f"This date was succesfully inputted: {start}")
  return start

def ending_date_func():
  if input("Would you like to use today's date as the final date?") == "yes":
    end = datetime.today()
    print(f"This date was succesfully inputted {end}")
    return end
  year = int(input("Enter the ending year: "))
  if year > 2021:
    print("Invalid starting year input.")
    return
  elif year < 1980:
    print("This system can't return weather data before 1980. Try again.")
  if input("Would you like to input a specific date? If not, then the 1st of January will be automatically be used.") == "yes":
    month = int(input("Input the month:"))
    day = int(input("Input the day: "))
    end = datetime(year, month, day)
    print(f"This date was succesfully inputted {end}")
  else:
    end = datetime(year, 1, 1)
    print(f"This date was succesfully inputted {end}")
  return end

