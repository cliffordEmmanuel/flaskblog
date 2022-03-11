from flask import Flask

# creates an object of the flask class
app = Flask(__name__)


# creates a route decorator
# this links the /home url to the welcome function
@app.route('/')
@app.route('/clifford')
@app.route('/home')
def Welcome():
    return "Clifford's personal"


if __name__ == "__main__":
    app.run(debug=True)

