# Makefile for Crate FastAPI server

.PHONY: app test coverage

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