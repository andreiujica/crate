# Makefile for Crate FastAPI server

.PHONY: app test coverage lint typecheck

# Run the FastAPI application
app:
	uv run -m uvicorn src.main:application --reload

# Run tests
test:
	PYTHONPATH=. uv run pytest

# Run tests with coverage
coverage:
	PYTHONPATH=. uv run pytest --cov=src --cov-report=term --cov-report=html
	@echo "HTML coverage report available at htmlcov/index.html" 

# Run linter
lint:
	uv run ruff check src tests 

# Run type checker
typecheck:
	PYTHONPATH=. uv run mypy --explicit-package-bases src tests 