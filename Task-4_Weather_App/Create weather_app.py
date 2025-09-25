from turtle import listen
import requests
import json
import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def pns(text):
    print(text)
    speak(text)

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("please try again...")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

def get_weather(api_key):
    # URL to get the weather data
    
    
    speak("Tell the city name whose weather to search:")
    city = listen()

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    # Make the GET request to OpenWeather API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant information from the JSON response
        city_name = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        feel_like = data['main']['feels_like']
        min_temp = data['main']['temp_min']
        max_temp = data['main']['temp_max']
        pressure = data['main']['pressure']
        weather_type = data['weather'][0]['main']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        visibility = data.get('visibility', 'N/A')
        cloudiness = data['clouds']['all']

        # Enter the weather details

        pns(f"Weather in {city_name}, {country}:")
        pns(f"Temperature: {temperature}°C")
        pns(f"Feels Like: {feel_like}°C")
        pns(f"Min Temperature: {min_temp}°C")
        pns(f"Max Temperature: {max_temp}°C")
        pns(f"Pressure: {pressure} hPa")
        pns(f"Weather Type: {weather_type}")
        pns(f"Weather Description: {weather_description}")
        pns(f"Humidity: {humidity}%")
        pns(f"Wind Speed: {wind_speed} meters per second")
        pns(f"Visibility: {visibility} meters")
        pns(f"Cloudiness: {cloudiness}%")
        pns("Thank you for using our free Weather App!\nPlease do visit again.")

        
        
    else:
        pns("City not found or invalid API key.")
       
# Main function
def main():
    api_key = '6235e46593cc91afe97a2631bf82afd5'  
    get_weather(api_key)

if __name__ == "__main__":
    main()

    
