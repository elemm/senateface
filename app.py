# http://flask.pocoo.org/
# https://dashboard.heroku.com/apps/dandan1111/deploy/heroku-git
# https://github.com/datademofun/heroku-basic-flask

import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)

def get_csv():
        csv_path = './static/115th congress spreadsheet - original-sunlight.csv'
        csv_file = open(csv_path, 'rb')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
        return csv_list


@app.route("/")
def homepage():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)


#@app.route("/<id>")

#<img src="https://theunitedstates.io/images/congress/225x275/{id}.jpg" alt="image">


#def redirect(id):
 #return <img src="https://theunitedstates.io/images/congress/450x550/{id}.jpg" alt="image">


if __name__ == "__main__":
    app.run()
