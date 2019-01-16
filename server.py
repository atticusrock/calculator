from os import environ
from flask import Flask

app = Flask(fuelcalculator)
app.run(environ.get('80'))