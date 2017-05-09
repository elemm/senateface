# http://flask.pocoo.org/
# https://dashboard.heroku.com/apps/dandan1111/deploy/heroku-git
# https://github.com/datademofun/heroku-basic-flask

import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)

def get_csv():
        csv_path = './static/115th congress spreadsheet - original-sunlight.csv'
        csv_file = open(csv_path, 'r') ## this means open as regular text not as "raw bytes"
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
        return csv_list

def get_house():
    rows = get_csv()
    houseppl = []

    for r in rows:
        if r['in_office'] == '1' and r['title'] == 'Rep':
            houseppl.append(r)
    return houseppl


def get_gender(gender):
    return [m for m in get_house() if m['gender'] == gender]



@app.route("/")
def homepage():
    congress = get_house()
    return render_template('index.html',congress=congress)


@app.route("/table")
def tablepage():
    return render_template('table.html', object_list=get_csv())


@app.route("/<id>")
def redirect(id):
    return render_template('reppage.html',rep_id=id,congress=get_house())


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
