from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['HEAD', 'OPTIONS', 'POST'], strict_slashes=False)
def index():
    """ Root
    """
    email = request.form.get('email', '')
    return "Your email is: {}".format(email)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
