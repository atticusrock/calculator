from os import environ
from flask import Flask

app = Flask(fuel)
app.run(environ.get('80'))