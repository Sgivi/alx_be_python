# Divide two values safely, handling errors like zero division and invalid numbers.

def safe_divide(numerator, denominator):
    
    # try to convert both input to numbers
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numerical values only."
    
    # check for division by zero
    try:
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."