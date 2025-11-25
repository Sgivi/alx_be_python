FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 

# Converts Fahrenheit to Celsius using the global factor
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Converts Celsius to Fahrenheit using global factor
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temp_input = input("Enter the temperature to convert: ").strip()
    
    if not temp_input.replace(".", "", 1).isdigit():
        raise ValueError("Invalid temperature. Please enter a numeric value.") 

    temperature = float(temp_input)
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result:.2f}°C")
        
    elif unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result:.2f}°F")
    else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

except ValueError as error:
    print(error)