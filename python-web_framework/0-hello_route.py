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

if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0 (accessible from any network interface) and port 5000
    app.run(host='0.0.0.0', port=5000)
