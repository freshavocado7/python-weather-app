import requests
import serial
from bs4 import BeautifulSoup
import config\


#Reading serial monitor from arduino
def readserial(comport, baudrate):
    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read

    while True:
        data = ser.readline().decode().strip()
        if data:
            print(data)
            exit()


#API SETUP
api_key = config.api_key
city = 'Gialova'
api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(api_url)

#SCRAPE SETUP
URL = "https://freemeteo.gr/kairos/gialova/o-kairos-tora/simeio/?gid=251358&language=greek&country=greece/" 
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser") 
results = soup.find(id="current-weather")
info_element = results.find_all("div", class_="last-renew-info")

for info_element in info_element:
    temp_element = info_element.find("div", class_="temp")
    print("freemeteo.gr Temperature in Gialova is:", end='')
    print(temp_element.text)


if response.status_code == 200:
    data = response.json()

    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    temp = temp-273.15
    print(f'OpenWeather Temperature in Gialova is: {temp:.2f}')
else:
    print('Error fetching weather data')

readserial('/dev/ttyUSB0', 115200)
