import requests

def get_weather(city):
    API_key = "e9a7701bef2ee52f9eb2f50aa7ee41b6"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data
    

def main():
    City_name = input("Enter city name: ")
    weather = get_weather(City_name)
    temp = weather['main']['temp']
    feel = weather['main']['feels_like']
    humidity = weather['main']['humidity']
    conditions = weather['weather'][0]['description']
    temp_min = weather['main']['temp_min']
    temp_max = weather['main']['temp_max']

    print(f"Temprature: {temp}°C \nFeels Like: {feel}°C\nConditions: {conditions}\nHumidity: {humidity}% \nTemprature Min {temp_min}°C\nTemprature Max {temp_max}°C")


main()

   
