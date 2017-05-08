# http://flask.pocoo.org/
# https://dashboard.heroku.com/apps/dandan1111/deploy/heroku-git
# https://github.com/datademofun/heroku-basic-flask

import csv
from flask import Flask
app = Flask(__name__)

@app.route("/")
def homepage():
    legislators = list(csv.DictReader(lines))
    legislators[index]
    <img src="https://theunitedstates.io/images/congress/225x275/{id}.jpg" alt="image">
    <a href="senateface.herokuapp.com/{id}">  Senator {name}
    </a>


@app.route("/<id>")
def redirect(id):
 return <img src="https://theunitedstates.io/images/congress/450x550/{id}.jpg" alt="image">



if __name__ == "__main__":
    app.run()
