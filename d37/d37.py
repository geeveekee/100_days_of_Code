from flask import Flask, render_template
from datetime import date
import requests

app = Flask(__name__)


@app.route('/')
def home_page():
    todays_date = date.today()
    name = "GeeKee"
    return render_template("index.html", date=todays_date, name=name)

@app.route('/guess/<name>')
def guess_gender_age(name):
    name = name
    data_for_age=requests.get(f"https://api.agify.io?name={name}")
    data_for_gender=requests.get(f"https://genderapi.io/api/?name={name}")
    return render_template("person.html", name=name, data=data_for_age.json(), gender=data_for_gender.json())
