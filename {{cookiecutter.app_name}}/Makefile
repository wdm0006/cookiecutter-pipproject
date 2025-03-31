.PHONY: install install-dev test test-cov lint lint-fix format clean build docs

install:
	uv pip install .

install-dev:
	uv pip install -e ".[dev]"

test:
	python -m pytest

test-cov:
	python -m pytest --cov={{cookiecutter.app_name}} --cov-report=html

lint:
	ruff check .
	ruff format --check .
	mypy {{cookiecutter.app_name}}

lint-fix:
	ruff check . --fix
	ruff format .

format: lint-fix

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	find . -type d -name "__pycache__" -exec rm -rf {} +

build:
	python -m build

docs:
	cd docs && make html 