def convert_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return "{:.2f}".format(celsius)


convert_to_celsius(100)
convert_to_celsius(-40)
convert_to_celsius(-459.67)
convert_to_celsius(32)
convert_to_celsius(98.6)