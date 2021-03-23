import requests
import json

class WeatherData(object):
    def __init__(self):
        self.alertData = ""
        self.currentWeather = ""

    def getData(self,city):
        city = str(city)
        getString = 'https://api.weatherbit.io/v2.0/current?city='+city+'&key=a049ffeb35c14e82b177b2b55cc740fe'
        alerts_request = requests.get(getString)
        json_alerts = json.loads(str(alerts_request.text))
        weatherData = self.parseAlerts(json_alerts)
        self.currentWeather = weatherData
       
    def parseAlerts(self,jsonData):
        cityName = "City: " + str(jsonData['data'][0]['city_name'])
        temp = (jsonData['data'][0]['temp'] * 9/5) + 32
        tempLine = "\nTemperature: " + str(temp) + "F"
        condition = "\nCurrent Weather: " + str(jsonData['data'][0]['weather']['description'])
        return cityName + tempLine + condition

def test(): #Quick debug function
    weather = WeatherData()
    weather.getData("Chicago")
    print(weather.currentWeather)

