from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

## Định nghĩa

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"
db = SQLAlchemy(app)

from .routes import *
from .models import *