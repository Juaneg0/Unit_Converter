def main_menu():
    print ("------ Units Converter ------")
    print("1. Convert temperature")
    print("2. Convert distance ")
    print("0. EXIT")
    choice = input("Enter your choice: ")
    return int(choice)

def temperature_menu():
    print("------ Temperature Conversion ------")
    print("1. Celcius to Fahrenheit")
    print("2. Fahrenheit to Celcius")
    choice = input("Enter your choice: ")
    return int(choice)