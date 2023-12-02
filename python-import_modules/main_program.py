# main_program.py

# Import the add function dynamically from 0-add.py
import importlib

# Replace "0-add" with the actual module name (without the .py extension)
module_name = "0-add"
add_module = importlib.import_module(module_name)
add = add_module.add

# Assign values to variables a and b


# Print the result using string format
