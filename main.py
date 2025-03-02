import Converters.Temperature as convert_Temperature
import menu

choice = 1
while choice != 0:
    choice = menu.main_menu()
    if choice == 1:
        choice = menu.temperature_menu()
        if choice == 1:
            Celcius = float(input("Enter a temperature in Celcius: "))
            Fahrenheit = convert_Temperature.celsius_to_fahrenheit(Celcius)
            print("Temperature in Fahrenheit: ", Fahrenheit)
        elif choice == 2:
            Fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
            Celcius = convert_Temperature.fahrenheit_to_celsius(Fahrenheit)
            print("Temperature in Celcius: ", Celcius)
