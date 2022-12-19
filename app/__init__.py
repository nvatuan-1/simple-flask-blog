from flask import Flask, render_template

## Định nghĩa

app = Flask(__name__)

from .routes import *