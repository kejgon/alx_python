"""Importing the Flask Framework

Keyword arguments:
argument -- description
Return: return_description
"""

from glob import escape
from flask import Flask
# Create a Flask application instance
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL.

    Returns:
        str: A string containing the "Hello HBNB!" message.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the root URL.

    Returns:
        str: A string containing the "Hello HBNB!" message.
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """
    Route handler for the '/c/<text>' URL.

    Args:
        text (str): The value of the 'text' variable from the URL.

    Returns:
        str: A string containing "C " followed by the value of the 'text' variable.
    """
    # Replace underscore (_) symbols with a space
    formatted_text = escape(text.replace('_', ' '))
    return f"C {formatted_text}"

if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0 (accessible from any network interface) and port 5000
    app.run(host='0.0.0.0', port=5000)
