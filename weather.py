weather = []

def check_weather():
    if not weather:
        print("Weather data is empty.")
    else:
        print("Weather data is available.")
        for data in weather:        print(f"Location: {data['location']}, Temperature: {data['temperature']}°C, Condition: {data['condition']},humidity: {data.get('humidity', 'N/A')}% ")

def enter_city_weather():
    location = input("Enter the city name: ")
    temperature = input("Enter the temperature (°C): ")
    condition = input("Enter the weather condition: ")
    humidity = input("Enter the humidity (%): ")
    weather.append({
        'location': location,
        'temperature': temperature,
        'condition': condition,
        'humidity': humidity
    })
    with open("weather.txt", "a") as file:
        file.write(f"{location},{temperature},{condition},{humidity}\n")

def search_city():
    city = input("Enter the city name to search: ")
    city_notfound = True
    for data in weather:
        if data['location'] == city:
            print(f"Location: {data['location']}, Temperature: {data['temperature']}°C, Condition: {data['condition']}, Humidity: {data.get('humidity', 'N/A')}%")
            city_notfound = False
    if city_notfound:
        print(f"No weather data found for {city}.")

def delete_city_weather():
    city = input("Enter the city name to delete: ")
    for i, data in enumerate(weather):
        if data['location'] == city:
            del weather[i]
            print(f"Weather data for {city} has been deleted.")
            return
    print(f"No weather data found for {city}.")

def update_city_weather():
    city = input("Enter the city name to update: ")
    for data in weather:
        if data['location'] == city:
            temperature = input("Enter the new temperature (°C): ")
            condition = input("Enter the new weather condition: ")
            humidity = input("Enter the new humidity (%): ")
            data['temperature'] = temperature
            data['condition'] = condition
            data['humidity'] = humidity
            print(f"Weather data for {city} has been updated.")
            return
    print(f"No weather data found for {city}.")

def count_cities():
    print(f"Total number of cities with weather data: {len(weather)}")

def hottest_city():
    if not weather:
        print("Weather data is empty.")
        return
    hottest = max(weather, key=lambda x: float(x['temperature']))
    print(f"The hottest city is {hottest['location']} with a temperature of {hottest['temperature']}°C.")

def  coldest_city():
    if not weather:
        print("Weather data is empty.")
        return
    coldest = min(weather, key=lambda x: float(x['temperature']))
    print(f"The coldest city is {coldest['location']} with a temperature of {coldest['temperature']}°C.")

def average_temperature():
    if not weather:
        print("Weather data is empty.")
        return
    avg_temp = sum(float(data['temperature']) for data in weather) / len(weather)
    print(f"The average temperature across all cities is {avg_temp:.2f}°C.")

def sort_cities_by_temperature():
    if not weather:
        print("Weather data is empty.")
        return
    sorted_weather = sorted(weather, key=lambda x: float(x['temperature']), reverse=True)
    print("Cities sorted by highest temperature:")
    for data in sorted_weather:
        print(f"Location: {data['location']}, Temperature: {data['temperature']}°C, Condition: {data['condition']}, Humidity: {data.get('humidity', 'N/A')}%")

def input_validation(prompt, validation_func):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print("Invalid input. Please try again.")

def exception_handling(func):
    try:
        func()
    except Exception as e:
        print(f"An error occurred: {e}")

def main_menu():
    while True:
        print("\nWeather Data Management System")
        print("1. Check Weather Data")
        print("2. Enter City Weather Data")
        print("3. Search City Weather Data")
        print("4. Delete City Weather Data")
        print("5. Update City Weather Data")
        print("6. Count Cities with Weather Data")
        print("7. Find Hottest City")
        print("8. Find Coldest City")
        print("9. Calculate Average Temperature")
        print("10. Sort Cities by Temperature")
        print("11. Exit")

        choice = input_validation("Enter your choice (1-11): ", lambda x: x.isdigit() and 1 <= int(x) <= 11)

        if choice == '1':
            exception_handling(check_weather)
        elif choice == '2':
            exception_handling(enter_city_weather)
        elif choice == '3':
            exception_handling(search_city)
        elif choice == '4':
            exception_handling(delete_city_weather)
        elif choice == '5':
            exception_handling(update_city_weather)
        elif choice == '6':
            exception_handling(count_cities)
        elif choice == '7':
            exception_handling(hottest_city)
        elif choice == '8':
            exception_handling(coldest_city)
        elif choice == '9':
            exception_handling(average_temperature)
        elif choice == '10':
            exception_handling(sort_cities_by_temperature)
        elif choice == '11':
            print("Exiting the program.")
            break
if __name__ == "__main__":
    main_menu() 