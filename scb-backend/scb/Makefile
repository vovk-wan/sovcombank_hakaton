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
fix_dump:
	./manage.py dumpdata auth.user --format=yaml > fixtures/user.yaml
	./manage.py dumpdata app_portfolio.CurrencyModel --format=yaml > fixtures/currency_model.yaml
	./manage.py dumpdata app_users.ProfileModel --format=yaml > fixtures/profile_model.yaml
	./manage.py dumpdata app_users.RoleModel --format=yaml > fixtures/role_model.yaml
	./manage.py dumpdata app_users.SubscriptionTypeModel --format=yaml > fixtures/subscribe_model.yaml

fix_load:
	./manage.py loaddata fixtures/user.yaml
	./manage.py loaddata fixtures/currency_model.yaml
	./manage.py loaddata fixtures/profile_model.yaml
	./manage.py loaddata fixtures/role_model.yaml
	./manage.py loaddata fixtures/subscribe_model.yaml
