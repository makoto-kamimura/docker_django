# docker_django
 
# new_project
* prod
docker-compose -f docker-compose.prod.yml run app django-admin startproject django_project .

# setting.py
* mysql

```
from pathlib import Path
# osのモジュールをインポート
import os

# [・・・]

# SECRET_KEYを.envから取得
SECRET_KEY = os.environ.get("SECRET_KEY")

# DEBUGを.envから取得
# envファイルにTrue、Falseと書くとDjangoがString型と認識してしまいます
# os.environ.get("DEBUG") == "True"を満たすとboolean型のTrueになり、
# env内のDEBUGがTrue以外ならFalseになります
DEBUG = os.environ.get("DEBUG") == "True"

# ALLOWED_HOSTSを.envから取得
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

# MySQLのパラメータを.envから取得
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        # コンテナ内の環境変数をDATABASESのパラメータに反映
        "NAME": os.environ.get("MYSQL_DATABASE"),
        "USER": os.environ.get("MYSQL_USER"),
        "PASSWORD": os.environ.get("MYSQL_PASSWORD"),
        "HOST": "db",
        "PORT": 3306,
    }
}

# 言語を日本語に設定
LANGUAGE_CODE = "ja"
# タイムゾーンをAsia/Tokyoに設定
TIME_ZONE = "Asia/Tokyo"

# STATIC_ROOTを設定
# Djangoの管理者画面にHTML、CSS、Javascriptが適用されます
STATIC_ROOT = "/static/"
STATIC_URL = "/static/"
```

# createsuperuser
docker exec -it "db_container_id" bash
```
python manage.py createsuperuser
Username (leave blank to use 'user1'): admin
Email address: admin@email.com
Password: # パスワードを入力
Password (again): 
This password is too common. # パスワードが単純過ぎる場合はエラー発生
Password: 
Password (again): 
Superuser created successfully.
```

# DB migrate
python manage.py makemigrations
python manage.py migrate

# deploy
* prod
docker-compose stop && docker-compose -f docker-compose.prod.yml build && docker-compose -f docker-compose.prod.yml up -d
* dev
docker-compose stop && docker-compose -f docker-compose.yml build && docker-compose -f docker-compose.yml up -d

# new_proogram
* docker exec -it "app_container_id" bash
python manage.py startapp analysis

* docker exec -it "app_container_id" bash
python manage.py startapp chatbot

# reference
https://qiita.com/shun198/items/f6864ef381ed658b5aba
https://qiita.com/tky2202026/items/f852461852de18ca92ff
