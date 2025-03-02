import menu
import Converters.Temperature as convert_Temperature
import Converters.Distance as convert_Distance
import Converters.Weight as convert_Weight


menu_choice = 1
while menu_choice != 0:
    menu_choice = menu.main_menu()
    if menu_choice == 1:
        temp_choice = menu.temperature_menu()
        if temp_choice == 1:
            Celcius = float(input("Enter a temperature in Celcius: "))
            Fahrenheit = convert_Temperature.celsius_to_fahrenheit(Celcius)
            print("Temperature in Fahrenheit: ", Fahrenheit)
        elif temp_choice == 2:
            Fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
            Celcius = convert_Temperature.fahrenheit_to_celsius(Fahrenheit)
            print("Temperature in Celcius: ", Celcius)
    elif menu_choice == 2:
        distance_choice = menu.distance_menu()
        if distance_choice == 1:
            Kilometer = float(input("Enter a distance in Kilometer: "))
            Mile = convert_Distance.kilometer_to_mile(Kilometer)
            print("Distance in Mile: ", Mile)
        elif distance_choice == 2:
            Mile = float(input("Enter a distance in Mile: "))
            Kilometer = convert_Distance.mile_to_kilometer(Mile)
            print("Distance in Kilometer: ", Kilometer)
    elif menu_choice == 3:
        weight_choice = menu.weight_menu()
        if weight_choice == 1:
            Kilogram = float(input("Enter a weight in Kilogram: "))
            Pound = convert_Weight.kilogram_to_pound(Kilogram)
            print("Weight in Pound: ", Pound)
        elif weight_choice == 2:
            Pound = float(input("Enter a weight in Pound: "))
            Kilogram = convert_Weight.pound_to_kilogram(Pound)
            print("Weight in Kilogram: ", Kilogram)
    