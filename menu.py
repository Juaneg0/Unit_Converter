def main_menu():
    print ("------ Units Converter ------")
    print("1. Convert temperature")
    print("2. Convert distance ")
    print("3. Convert weight")
    print("0. EXIT")
    choice = input("Enter your choice: ") 
    return int(choice)

def temperature_menu():
    print("------ Temperature Conversion ------")
    print("1. Celcius to Fahrenheit")
    print("2. Fahrenheit to Celcius")
    choice = input("Enter your choice: ")
    return int(choice)

def distance_menu():
    print("------ Distance Conversion ------")
    print("1. Kilometer to Mile")
    print("2. Mile to Kilometer")
    choice = input("Enter your choice: ")
    return int(choice)

def weight_menu():
    print("------ Weight Conversion ------")
    print("1. Kilogram to Pound")
    print("2. Pound to Kilogram")
    choice = input("Enter your choice: ")
    return int(choice)
