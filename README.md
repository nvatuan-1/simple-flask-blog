# Cài đặt
1. Tạo môi trường ảo
    - Chạy câu lệnh: `python -m venv venv`
    - Bật môi trường ảo: `venv\Scripts\activate.bat` -> Có chữ venv

### Nếu đã có file `requirements.txt`
2a. Cài đặt thư viện được share
    - Chạy câu lệnh `pip install -r requirements.txt`

### Nếu chưa có file `requirements.txt`
2b. Cài `Flask` lên môi trường ảo
    - Chạy câu lệnh: `pip install Flask`

## Giữ trạng thái môi trường
Trong quá trình code, và cài thư viện, thư mục `venv` có thể lên đến vài GB. Ta không thể share thư mục này, chỉ có thể share phiên bản của các thư viện. Để share phiên bản, thì dùng câu lệnh: `pip freeze > requirements.txt`

# Chạy project

## Bật biến môi trường
- `venv\Scripts\activate`

## Setup biến môi trường
```
set FLASK_APP=app.py
set FLASK_DEBUG=1
```

## Chạy server
- `flask run`
-> Nhấp vào đường link [http://127.0.0.1:5000](http://127.0.0.1:5000) để thưởng thức.


<!-- # Làm việc với git
1. Khởi tạo project với git: `git init`
2. Liên kết project `local` với project online trên GitHub.
    - Chạy câu lệnh: `git remote add origin <link_github_project>`
        Trong trường hợp này là: `git remote add origin https://github.com/nvatuan-1/simple-flask-blog.git`
3. Tạo nhánh, lần đầu thì tạo nhánh `main`
    - Chạy câu lệnh: `git branch -M main` -->