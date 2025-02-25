import Converters.Temperature as convert_Temperature


print ("------ Units Converter ------")
Celcius = float(input("Enter a temperature in Celcius: "))
Fahrenheit = convert_Temperature.celsius_to_fahrenheit(Celcius)

print("Temperature in Fahrenheit: ", Fahrenheit)
