докер контейнер для постгрес
docker run --name postgres_django -p 5432:5432 -e POSTGRES_PASSWORD=123456 -d postgres

docker restart postgres_django

python3 manage.py createsuperuser
superuser admin password 123456

створення міграцій
python3 manage.py makemigrations
python3 manage.py migrate


перенесення бази з Монго в Постргрес
python3 -m quotes_project.migration


запуск
python3 manage.py runserver 