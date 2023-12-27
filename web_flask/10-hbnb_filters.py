#!/usr/bin/python3

"""Script launches an online Flask application."""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """shows the HTML page for the HBnB filters."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(excpt=None):
    """Take SQLAlchemy Session out of running."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
