def convert_to_celsius_1(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

def convert_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return round(celsius, 2)



convert_to_celsius_1(100)
convert_to_celsius(-40)
convert_to_celsius(-459.67)
convert_to_celsius(32)
convert_to_celsius(98.6)