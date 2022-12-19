from . import app
from flask import render_template
from .services import add_two_number

### Điều hướng

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/math/<int:num_a>/<int:num_b>')
def math(num_a: int, num_b: int):
    ans = add_two_number(num_a, num_b)
    params = dict(num_a=num_a, num_b=num_b, ans=ans)
    return render_template('math.html', **params)