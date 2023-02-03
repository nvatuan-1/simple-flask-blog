import sys
import json
from app import db, app

def init_db():
    '''
        Khoi tao database
    '''
    with app.app_context():
        db.drop_all() # bo tat ca table cu
        db.create_all() # tao lai moi

        from app.models import User, Post

        user = User(username="admin",
                    password="admin123",
                    name="Admin",
                    email="admin@gmail.com")

        # them vao database
        db.session.add(user)
        # xac nhan
        db.session.commit()

        dummy_posts = json.load(open('dummy_data\post.json', 'r', encoding='utf-8'))
        for post_data in dummy_posts:
            post = Post(**post_data) # unpacking dictionary
            db.session.add(post)
            db.session.commit()

    print("Create db successfully!")

if len(sys.argv) < 2:
    print("Ban khong goi gi ca!")
else:
    func_name = sys.argv[1]

    eval(func_name)()