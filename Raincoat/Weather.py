import requests
from bs4 import BeautifulSoup

print('Welcome to Raincoat')
#print('Please enter your zip code:')
#zipcode = input()

#URL = "https://www.weather.gov/rah/"
URL = "https://forecast.weather.gov/MapClick.php?lon=-78.64154034128245&lat=35.789604836866715#.Yeywy-rMJD8"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

forecast = soup.find(id="current_conditions-summary")
#print(forecast.prettify())

temperature = forecast.find( class_="myforecast-current-lrg")
low = forecast.find( class_="myforecast-current-sm")
print("Current temperature is " + temperature.text)
print("The low for today is " + low.text)