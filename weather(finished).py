# import requests
import requests
from datetime import datetime

# api key
api_key = "ebf3d83100066ce06b81be2ed6008685"

# urls
url = "https://api.openweathermap.org/data/2.5/weather?lat=45.52&lon=-122.67&appid=ebf3d83100066ce06b81be2ed6008685"
url2 = "https://api.openweathermap.org/data/2.5/forecast?lat=45.52&lon=-122.67&appid=ebf3d83100066ce06b81be2ed6008685"

# send get request at url
r = requests.get(url)
r2 = requests.get(url2)

# display json weather data returned by api
print(r.json)
print(r2.json)

# store returned json data 
data = r.json()
data2 = r2.json()

# check if it's raining in Portland
def check_rain(data):
    weather_list = data.get("weather",[])
    print(weather_list)

    for weather_item in weather_list:
        main_condition = weather_item.get("main","").lower()
        if main_condition == "rain":
            return True
    
    if "rain" in data:
        print("It is currently raining in Portland")
        return True
    else:
        print("It is currently not raining in Portland")
        return False

# check three day forecast  
def rain_forecast(data2):
    forecast_list = data2.get("list", [])
    for forecast in forecast_list[:24]:  # ~3 days worth (8 entries per day)
            weather_conditions = forecast.get("weather", [])
            timestamp = forecast.get("dt_txt", "N/A")

            for condition in weather_conditions:
                main_condition = condition.get("main", "").lower()
                if "rain" in main_condition:
                    print(f"☔ Rain is forecast at {timestamp}")
                    return True  # Stop after the first match

    print("No rain is forecast in the next 3 days.")
    return False
    
if __name__ == "__main__":
    check_rain(data)
    rain_forecast(data2)
    
    



