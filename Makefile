.PHONY: install dev clean format lint test coverage run migrate

# Python environment variables
PYTHON_VERSION := 3.9
VENV := .venv
PYTHON := $(VENV)/bin/python
UV := $(VENV)/bin/uv
RUFF := $(VENV)/bin/ruff
PYTEST := $(VENV)/bin/pytest
ALEMBIC := $(VENV)/bin/alembic

install:
	uv venv --python=$(PYTHON_VERSION)
	$(UV) pip install -e .

dev: install
	$(UV) pip install -e ".[dev]"

clean:
	rm -rf $(VENV)
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf .ruff_cache
	rm -rf __pycache__
	rm -rf **/__pycache__
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist

format:
	$(RUFF) check --fix .
	$(RUFF) format .

lint:
	$(RUFF) check .

test:
	$(PYTEST)

coverage:
	$(PYTEST) --cov=app --cov-report=html

run:
	uvicorn main:app --reload --port 8000

# Database migrations
migrate-init:
	$(ALEMBIC) init alembic

migrate-create:
	$(ALEMBIC) revision --autogenerate -m "$(message)"

migrate-up:
	$(ALEMBIC) upgrade head

migrate-down:
	$(ALEMBIC) downgrade -1

.env:
	cp .env.example .env

setup: clean .env dev migrate-up
	@echo "Development environment setup complete!"
