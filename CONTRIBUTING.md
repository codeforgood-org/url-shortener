# Contributing to Todo List Manager

Thank you for your interest in contributing to the Todo List Manager! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:

1. A clear, descriptive title
2. Steps to reproduce the issue
3. Expected behavior
4. Actual behavior
5. Your environment (OS, Python version)
6. Any relevant error messages or logs

### Suggesting Enhancements

We welcome feature suggestions! Please create an issue with:

1. A clear description of the feature
2. Why this feature would be useful
3. Example use cases
4. Any implementation ideas you have

### Pull Requests

We love pull requests! Here's how to submit one:

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Add tests** if you've added functionality
4. **Ensure tests pass** by running the test suite
5. **Update documentation** if needed
6. **Submit a pull request** with a clear description

## Development Setup

### Prerequisites

- Python 3.6 or higher
- Git

### Setting Up Your Development Environment

1. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/url-shortener.git
cd url-shortener
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -e ".[dev]"
```

Or if using pip with requirements.txt:
```bash
pip install pytest pytest-cov black flake8 mypy
```

## Coding Standards

### Python Style Guide

This project follows PEP 8 style guidelines. Key points:

- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use descriptive variable names
- Add docstrings to all functions and classes
- Use type hints where appropriate

### Code Formatting

We use `black` for code formatting:

```bash
black todo.py tests/ examples/
```

### Linting

We use `flake8` for linting:

```bash
flake8 todo.py tests/ examples/
```

### Type Checking

We use `mypy` for type checking:

```bash
mypy todo.py
```

## Testing

### Running Tests

Run all tests:
```bash
python -m pytest tests/
```

Run tests with coverage:
```bash
python -m pytest --cov=todo tests/
```

Run tests verbosely:
```bash
python -m pytest -v tests/
```

### Writing Tests

- Place test files in the `tests/` directory
- Name test files as `test_*.py`
- Name test functions as `test_*`
- Use descriptive test names that explain what is being tested
- Each test should test one specific behavior
- Use setUp and tearDown for test fixtures

Example test structure:
```python
def test_add_task_success(self):
    """Test that adding a valid task succeeds."""
    result = self.manager.add_task("Test task")
    self.assertTrue(result)
    tasks = self.manager.load_tasks()
    self.assertEqual(len(tasks), 1)
```

## Documentation

### Code Documentation

- Add docstrings to all public functions, classes, and modules
- Use Google-style docstrings
- Include parameter types and return types
- Provide usage examples where helpful

Example:
```python
def add_task(self, description: str) -> bool:
    """
    Add a new task to the list.

    Args:
        description: Task description

    Returns:
        True if successful, False otherwise

    Example:
        >>> manager = TodoManager()
        >>> manager.add_task("Buy groceries")
        True
    """
    pass
```

### README Updates

If your change adds new features or changes existing behavior:

1. Update the README.md with new usage examples
2. Update the feature list if applicable
3. Add any new dependencies to requirements.txt

## Commit Messages

Write clear, descriptive commit messages:

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- First line should be 50 characters or less
- Reference issues and pull requests when relevant

Good examples:
```
Add priority support to tasks
Fix bug in task removal logic
Update documentation for new clear command
```

## Branch Naming

Use descriptive branch names:

- `feature/add-priority-support`
- `bugfix/fix-task-removal`
- `docs/update-readme`
- `test/add-manager-tests`

## Release Process

(For maintainers)

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md with release notes
3. Create a git tag: `git tag -a v1.0.0 -m "Release v1.0.0"`
4. Push tag: `git push origin v1.0.0`
5. Create GitHub release with release notes

## Getting Help

If you need help with your contribution:

1. Check existing documentation and issues
2. Create a new issue with your question
3. Be specific about what you're trying to do
4. Include relevant code snippets or error messages

## Recognition

All contributors will be recognized in the project. Thank you for your contributions!

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.
