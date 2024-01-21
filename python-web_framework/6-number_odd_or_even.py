"""Importing the Flask Framework

Keyword arguments:
argument -- description
Return: return_description
"""
from flask import Flask, render_template

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
    Route handler for the '/hbnb' URL.

    Returns:
        str: A string containing the "HBNB" message.
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
    return f"C {text.replace('_', ' ')}"

@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """
    Route handler for the '/python/<text>' URL.

    Args:
        text (str): The value of the 'text' variable from the URL. Defaults to 'is_cool'.

    Returns:
        str: A string containing "Python " followed by the value of the 'text' variable.
    """
    # Replace underscore (_) symbols with a space
    return f"Python {text.replace('_', ' ')}"

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route handler for the '/number/<n>' URL.

    Args:
        n (int): The value of the 'n' variable from the URL.

    Returns:
        str: A string containing "n is a number" only if n is an integer.
    """
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route handler for the '/number_template/<n>' URL.

    Args:
        n (int): The value of the 'n' variable from the URL.

    Returns:
        str: A rendered HTML page with an H1 tag containing "Number: n" if n is an integer.
    """
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route handler for the '/number_odd_or_even/<n>' URL.

    Args:
        n (int): The value of the 'n' variable from the URL.

    Returns:
        str: A rendered HTML page with an H1 tag containing "Number: n is even|odd" if n is an integer.
    """
    odd_or_even = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, odd_or_even=odd_or_even)

if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0 (accessible from any network interface) and port 5000
    app.run(host='0.0.0.0', port=5000)
