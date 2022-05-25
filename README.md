# 仕様
ブログアプリ

# 要件定義
* 管理者ユーザー
    * ログイン, ログアウト
    * ブログのCRUD
* アノニマスユーザー
    * ブログの閲覧

# 環境
Python_______
django_______


# 動かす際
* python manage.py makemigrations customauth
* python manage.py makemigrations blog
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver

# root url
* blog/


