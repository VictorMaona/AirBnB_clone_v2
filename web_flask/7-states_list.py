#!/usr/bin/python3
"""Script launches an online Flask application."""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exc):
    """To end SQLAlchemy session use the teardown method."""
    storage.close()


@app.route('/states_list')
def states_list():
    """Show an HTML page listing every State object."""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
