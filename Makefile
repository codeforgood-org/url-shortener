.PHONY: help install install-dev test test-verbose test-coverage lint format type-check clean run examples security all

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install the package
	pip install -e .

install-dev: ## Install development dependencies
	pip install -e ".[dev]"
	pip install pytest pytest-cov black flake8 mypy bandit safety pre-commit

test: ## Run tests
	python -m pytest tests/ -v

test-verbose: ## Run tests with verbose output
	python -m pytest tests/ -vv

test-coverage: ## Run tests with coverage report
	python -m pytest --cov=todo --cov-report=html --cov-report=term tests/
	@echo "Coverage report generated in htmlcov/index.html"

lint: ## Run linting checks
	flake8 todo.py tests/ examples/ --max-line-length=100 --extend-ignore=E203

format: ## Format code with black
	black todo.py tests/ examples/

format-check: ## Check code formatting without modifying files
	black --check todo.py tests/ examples/

type-check: ## Run type checking with mypy
	mypy todo.py --ignore-missing-imports

security: ## Run security checks
	bandit -r todo.py
	pip freeze | safety check --stdin || true

clean: ## Clean up generated files
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	find . -type f -name '*.coverage' -delete
	find . -type d -name '*.egg-info' -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name 'htmlcov' -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name '.pytest_cache' -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name '.mypy_cache' -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name 'tasks.json' -delete
	find . -type f -name 'example_tasks.json' -delete
	find . -type f -name 'advanced_tasks.json' -delete
	@echo "Cleaned up generated files"

run: ## Run the todo application (use: make run ARGS="list")
	python todo.py $(ARGS)

examples: ## Run example scripts
	@echo "Running basic usage example..."
	python examples/basic_usage.py
	@echo ""
	@echo "Running advanced usage example..."
	python examples/advanced_usage.py

pre-commit-install: ## Install pre-commit hooks
	pre-commit install

pre-commit-run: ## Run pre-commit on all files
	pre-commit run --all-files

all: clean format lint type-check test ## Run all checks (format, lint, type-check, test)
	@echo "All checks passed!"

ci: lint type-check test ## Run CI checks (lint, type-check, test)
	@echo "CI checks passed!"

.DEFAULT_GOAL := help
