install:
	poetry install

build:
	poetry build

publish:
	poetry publish -r test

lint:
	poetry run flake8 page_loader tests

test:
	poetry run pytest --cov=gendiff --cov-report xml tests/