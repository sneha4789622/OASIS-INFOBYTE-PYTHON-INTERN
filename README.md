Python Programming Internship @OasisInfobyte
# Project Title

## Task-1: 🗣 Smart Voice Assistant
A Python-based voice-controlled assistant that can respond to greetings, tell the time/date, search Google/Wikipedia, open selected websites and more — all through simple voice commands.

### 📌 Features
- Responds to greetings like *"Hello"* 👋
- Tells you the *current time* ⏰
- Tells you the *current date* 📅
- Performs *Google/Wikipedia searches* 🔍
- Opens selected websites (*Google, YouTube, LinkedIn*) 🌐
- Ends session when you say *"quit"* 🚪

### 📦 Modules Used and Their Purpose

| Module | Purpose |
|--------| --------|
| pyttsx3 | Converts text to speech for audio responses |
| speech_recognition | Captures and recognizes voice input |
| datetime | Gets the current date and time |
| time | Adds delays between operations |
| wikipedia | Fetches quick summaries from Wikipedia |
| webbrowser | Opens websites in the default browser |

---

### ⚙ Functions in the Project

| Function | Description |
|----------|-------------|
| speak(audio) | Speaks the given text aloud |
| pns(text) | Prints and speaks text together |
| WishMe() | Greets the user based on the current time |
| actual_date() | Tells the current date |
| takeCommand() | Listens to the user's voice and converts it to text |
| main() | Main loop that listens and executes commands |

---

### 🚀 How to Run

1. *Install VS code* (v3.8 or above recommended)
2. *Install the required modules* using pip:

  ```
     pip install pyttsx3 SpeechRecognition wikipedia
  ```
3. Save the project code as voice_assistant.py
4. Run the script:
   ```
   python voice_Assistant.py
   ```
5. Start speaking commands like:
- "Hello"
- "tell me the time?"
- "What is the date?"
- "Wikipedia"
- "Open website"
- "quit"

---

### 💡 Example Usage

```
User: Hello
Assistant: Hello Mam, I'm your Personal Voice Assistant! Please tell me how may I help you

User: What is the date
Assistant: The date is 25th of September of year 2025

User: Open website
Assistant: Which website would you like me to open?
```
---
---
---

## Task-2: BMI Calculator 🧮

A Python program to calculate **Body Mass Index (BMI)** with **realistic input limits** and robust **exception handling**.

---

### 📌 Features
- Takes **weight (kg)** and **height (m)** from the user


- Categorizes BMI into:
  - Underweight
  - Normal Weight
  - Overweight
  - Obese (with Obesity Classes I, II, and III)
- Keeps prompting until valid values are entered

---

### 🧠 BMI Categories Reference

| BMI Value     | Category                       |
|---------------|--------------------------------|
| < 18.5        | Underweight                    |
| 18.5 – 24.9   | Normal Weight                  |
| 25 – 29.9     | Overweight                     |
| 30 – 35       | Obesity Class I                  |
| 35 – 40       | Obesity Class II               |
| ≥ 40          | Obesity Class III (Severe)     |

---

### 📂 Code Overview
 - Takes weight in kilograms
 - Takes height in metres
 - Validation for positive numeric values
 - category classification then details Obesity Classes
 - height Calculation:
  ```
  height_in_meters = height / 100

  ```


- BMI Calculation:
```
bmi =  weight / (height_in_meters ** 2)

```
- BMI Categorization: Uses conditional statements to determine BMI category.

---

### 🖥️ How to Run

1. Run the program in your terminal:
   ```
   python bmi_calculator.py
   ```
---

### 📜 Example Output
```
Enter your weight (in kg): 72
Enter your height (in m): 178

Your Body Mass Index is: 22.72
Your BMI Category is:
You are Healthy (Normal Weight)!
```
---
---
---

## Task-3: 🔐 Random Password Generator

A simple Python program to generate **random secure passwords** based on user preferences for letters, numbers, and symbols.  
The program includes **basic exception handling** to avoid crashes when users enter invalid inputs.

---

### 📌 Features
- User specifies:
  - Password length
  - Whether to include **letters**
  - Whether to include **numbers**
  - Whether to include **symbols**
- Validates inputs:
  - Ensures only integers are entered
  - Ensures options are `1 (Yes)` or `0 (No)`
  - At least one character type must be selected
- Generates a password of the requested length using the selected character sets
---
### 📂 Code Overview
- Main function: Handles the whole process
- generate_passwords() → Handles user input with try-except for invalid integers.
  - Validates only 0/1 for choices
  - Ensures at least one option is selected
- Password Generation:
```
for i in range(length):
    password += random.choice(choices)
```
---

### 🖥️ How to Run
1. Clone this repository or download the Python file:
   ```
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator
   ```
2. Run the script:
   ```
   python password_generator.py
    ```
---
### 📜 Example Output
   ```
   Enter the length of your password: 6
   Do you want letters in your password? (1 for Yes, 0 for No): 1
   Do you want numbers in your password? (1 for Yes, 0 for No): 1
   Do you want symbols in your password? (1 for Yes, 0 for No): 0

   Your random generated password of length 6 is: 47GJzU
   ```
---
---
---

## Task-4: 🌦️ Voice-Powered Weather App

This is a Python-based Weather Application that uses the **functions from Task 1 (Smart Voice Assistant)** to fetch real-time weather data from the [OpenWeatherMap API](https://openweathermap.org/api) and **speak it aloud to the user**.  

You can simply say the **city name**, and the app will fetch and narrate details like temperature, weather condition, humidity, and wind speed.

---

### 📌 Features
- Takes **voice input** of the city name 🎤  
- Fetches **real-time weather data** from OpenWeatherMap 🌍  
- Speaks out:  
  - City & Country  
  - Temperature (Current, Feels Like, Min, Max) 🌡️  
  - Weather Type & Description ☁️  
  - Humidity 💧  
  - Wind Speed 💨  
- Error handling for invalid requests ❌  

---

### 📦 Modules Used

| Module | Purpose |
|--------|---------|
| `requests` | To make HTTP requests to the OpenWeatherMap API |
| `json` (via requests) | Parse weather data from API response |
| `pyttsx3` | Converts text to speech for audio responses |
| `speech_recognition` | Captures and recognizes voice input |

---

### ⚙️ How It Works
1. The app asks you to **speak the city name**.  
2. It sends the request to the **OpenWeatherMap API**.  
3. API returns the weather details in JSON format.  
4. The program extracts and **speaks the details** to the user.  

---

### 🔑 Getting Your Own API Key
To use this project, you need an API key from OpenWeatherMap.  

1. Go to 👉 [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)  
2. Create a free account and log in.  
3. Navigate to the **API Keys** section in your profile.  
4. Copy your **API Key**.  
5. Replace `<Your-API-Key>` in the code with your actual key:
   ```
   API_KEY = "your_api_key_here"
   ```

   ---

### 🚀 How to Run
1. Install Python (v3.8 or higher recommended).
2. Install the required module:
   ```
   pip install requests pyttsx3 speech_recognition
   ```
3. Save the file as weather_app.py.
4. Run the program:
   ```
   python weather_app.py
   ```
6. Speak the city name when prompted. 🎙️

---

### 💡 Example Usage
   ```
Assistant: Tell the city name whose weather to search:  
User: London  

Assistant:  
Weather in London, GB:  
Temperature: 18°C  
Feels like: 16°C  
Minimum Temperature: 15°C  
Maximum Temperature: 20°C  
Weather Type: Clouds  
Weather Condition: Scattered Clouds  
Humidity: 72%  
Wind Speed: 3.5 metres per second  
   ```

---

### 🛡 Notes
- Requires an internet connection to fetch live data.
- Make sure your microphone is working for voice input.

---














  


