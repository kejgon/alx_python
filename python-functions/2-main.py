convert_to_celsius = __import__('2-temperature').convert_to_celsius

print("{:.2f}".format(convert_to_celsius(100)))
print(convert_to_celsius(-40))
print("{:.2f}".format(convert_to_celsius(-459.67)))
print(convert_to_celsius(32))