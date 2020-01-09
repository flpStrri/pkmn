it: test

build: build/install-dependencies

build/install-dependencies:
	pipenv install --dev --ignore-pipfile

test: build test/code-style test/run

test/code-style:
	pipenv run mypy application/ domain/ service/

test/run:
	pipenv run pytest --cov=. --no-cov-on-fail tests/
