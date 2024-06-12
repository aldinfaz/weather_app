import requests
import tkinter as tk

api_key = "a2811e34c16e69053249665820876507"

def on_button_click():
    city = entry.get()

    weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        label.config(text = "No city found", bg = "lightblue")
    
    else:
        entry.destroy()
        button.destroy()

        weather = weather_data.json()['weather'][0]['main']
        temperature = round(weather_data.json()['main']['temp'])

        label.config(text = city)

        weather_label = tk.Label(root, text = f'The weather in {city} is: {weather}', bg = "lightblue")
        temp_label = tk.Label(root, text = f'The temperature in {city} is: {temperature}°C', bg = "lightblue")

        weather_label.place(x = 305, y = 30)
        temp_label.place(x = 305, y = 55)

#GUI
root = tk.Tk()
root.title = "Aldin's Weather App"
root.geometry("800x150")
root.configure(bg = "lightblue")

label = tk.Label(root, text = "Enter your city below", bg = "lightblue")
label.pack(pady=10)

entry = tk.Entry(root, bg = "lightblue", fg = "white")
entry.place(x = 305, y = 50)

#button isnt flush with window background but whatever
button = tk.Button(root, text="Enter", command=on_button_click, bg = "lightblue", borderwidth=0, highlightthickness=0, relief='flat')
button.place(x = 365, y = 100)

#run
root.mainloop()