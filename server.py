from os import environ
from flask import Flask
import fuel_calc

app = Flask(fuel_calc)
app.run(environ.get('80'))