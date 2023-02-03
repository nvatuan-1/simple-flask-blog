from . import app
from flask import render_template
from .models import *
# from .services import add_two_number

### Điều hướng

@app.route('/')
def home():

    # gia su
    user_id = 1
    # # lấy user đầu tiên có id là user_id
    # user = User.query.filter(id=user_id).first()

    # lấy tất cả post được tạo bởi user_id
    pagination = Post.query.filter_by(user_id=user_id).paginate(page=1, per_page=4)

    all_posts = []
    for page_num in pagination.iter_pages():
        all_posts.append(pagination.items)
        pagination = pagination.next()

    # truyền các biến xuống render_template
    return render_template('home.html', all_posts=all_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/content/<int:post_id>')
def content(post_id: int):
    post = Post.query.filter_by(id=post_id).first()
    return render_template('content.html', post=post)

# @app.route('/math/<int:num_a>/<int:num_b>')
# def math(num_a: int, num_b: int):
#     ans = add_two_number(num_a, num_b)
#     params = dict(num_a=num_a, num_b=num_b, ans=ans)
#     return render_template('math.html', **params)