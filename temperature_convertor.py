# Task: Temperature Converter

#------------------------------------------------------

# Requirements:

# User Interface: Create a basic command-line interface (CLI) for the temperature converter application.

# Conversion Options: Allow the user to choose between converting from Celsius to Fahrenheit or from Fahrenheit to Celsius.

# Input: Prompt the user to enter the temperature value.

# Perform Conversion: Based on the user's choice, perform the appropriate temperature conversion.

# Display Result: Print out the converted temperature value.

# Handle Invalid Inputs: Ensure that the user enters a valid numeric temperature value.

# Documentation: Include comments in your code to explain the purpose of functions and any complex logic.

# Testing: Test your program with various inputs to ensure it performs the conversions correctly and handles invalid inputs gracefully.

#------------------------------------------------------
# CODING SECTION:
#------------------------------------------------------


def get_temperature_input():
    try:
        temperature = float(input("Enter the temperature: "))
        return temperature
    except ValueError:
        print("Value Error!")
        exit(1)

def get_temperature_type_input(message):
    temperature_type = str(input(message)).capitalize()
    if temperature_type not in ["K", "F", "C"]:
        print("Enter a valid type of temperature!")
        exit(1)
    return temperature_type

def check_absolute_zero(temperature, temperature_type):
    if temperature_type == "K" and temperature < 0:
        print("The temperature value cannot be less than absolute 0!")
        exit(1)
    elif temperature_type == "F" and temperature < -459.67:
        print("The temperature value cannot be less than absolute -459.67!")
        exit(1)
    elif temperature_type == "C" and temperature < -273.15:
        print("The temperature value cannot be less than absolute -273.15!")
        exit(1)

def convert_temperature(entered_temperature, selected_temperature_type, converting_temperature_type):
    if selected_temperature_type == converting_temperature_type:
        return entered_temperature

    if selected_temperature_type == "K":
        if converting_temperature_type == "F":
            return (entered_temperature - 273.15) * 9/5 + 32
        elif converting_temperature_type == "C":
            return entered_temperature - 273.15
    elif selected_temperature_type == "F":
        if converting_temperature_type == "K":
            return (entered_temperature - 32) * 5/9 + 273.15
        elif converting_temperature_type == "C":
            return (entered_temperature - 32) * 5/9
    elif selected_temperature_type == "C":
        if converting_temperature_type == "K":
            return entered_temperature + 273.15
        elif converting_temperature_type == "F":
            return entered_temperature * 9/5 + 32

def main():
    entered_temperature = get_temperature_input()
    selected_temperature_type = get_temperature_type_input("Which type of temperature did you enter: (K, F, C)")
    check_absolute_zero(entered_temperature, selected_temperature_type)

    converting_temperature_type = get_temperature_type_input("Which type of temperature do you want to convert: (K, F, C)")

    converted_temperature = convert_temperature(entered_temperature, selected_temperature_type, converting_temperature_type)

    print(f"The converted value of entered {entered_temperature} {selected_temperature_type} degree is {converted_temperature} {converting_temperature_type} degree.")

if __name__ == "__main__":
    main()
        