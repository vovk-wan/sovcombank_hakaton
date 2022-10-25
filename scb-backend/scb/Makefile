run:
	./manage.py runserver 127.0.0.1:8887
migrate:
	./manage.py makemigrations
	./manage.py migrate
lint:
	isort --profile=black .
	black .
celery:
	celery -A scb worker -l INFO -c 2