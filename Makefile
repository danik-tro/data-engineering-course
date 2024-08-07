.PHONY: setup \
		run \
		test \

virtual_env:
	python -m venv venv

setup: virtual_env
	. venv/bin/activate; pip install --upgrade pip
	. venv/bin/activate; pip install poetry
	. venv/bin/activate; poetry install
	. venv/bin/activate; pre-commit install

test:
	. venv/bin/activate; python -m pytest -vv

coverage:
	. venv/bin/activate; python -m pytest -vv --cov=dem tests/ --no-cov-on-fail --tb=no tests/

fmt:
	. venv/bin/activate; ruff format
	. venv/bin/activate; ruff check --fix
	. venv/bin/activate; ruff format

check:
	. venv/bin/activate; ruff check
	. venv/bin/activate; ruff format --check
	. venv/bin/activate; mypy .

mypy:
	. venv/bin/activate; mypy .

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -f .coverage
	rm -fr htmlcov/
