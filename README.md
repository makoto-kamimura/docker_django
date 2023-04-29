# docker_django
 
# new
* prod
docker-compose -f docker-compose.prod.yml run app django-admin startproject django_project .
* dev
docker-compose -f docker-compose.yml run app django-admin startproject djangopj .

# 
* prod
docker-compose -f docker-compose.prod.yml build
* dev
docker-compose -f docker-compose.yml build

#
* prod
docker-compose -f docker-compose.prod.yml up -d

* dev
docker-compose -f docker-compose.yml up -d

https://qiita.com/shun198/items/f6864ef381ed658b5aba