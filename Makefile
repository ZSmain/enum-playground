.PHONY: install
install:
	uv sync

.PHONY: migrate
migrate:
	uv run python manage.py migrate

.PHONY: makemigrations
makemigrations:
	uv run python manage.py makemigrations

.PHONY: runserver
runserver:
	uv run python manage.py runserver

.PHONY: createsuperuser
createsuperuser:
	uv run python manage.py createsuperuser

.PHONY: test
test:
	uv run python manage.py test

.PHONY: collectstatic
collectstatic:
	uv run python manage.py collectstatic

.PHONY: shell
shell:
	uv run python manage.py shell
