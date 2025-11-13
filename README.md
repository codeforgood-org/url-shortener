# Todo List Manager

A simple, lightweight command-line todo list manager written in Python. Manage your tasks efficiently from the terminal with easy-to-use commands.

## Features

- Add new tasks with descriptions
- List all tasks with numbered indices
- Remove completed tasks by number
- Persistent storage using JSON
- Simple and intuitive command-line interface
- No external dependencies (pure Python)

## Installation

### Requirements

- Python 3.6 or higher

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/codeforgood-org/url-shortener.git
cd url-shortener
```

2. Make the script executable (optional):
```bash
chmod +x todo.py
```

3. Start using it immediately:
```bash
python todo.py list
```

## Usage

### Add a Task

Add a new task to your todo list:

```bash
python todo.py add "Buy groceries"
python todo.py add "Complete project documentation"
```

### List All Tasks

Display all tasks with their numbers:

```bash
python todo.py list
```

Example output:
```
1. Buy groceries
2. Complete project documentation
3. Call dentist for appointment
```

### Remove a Task

Remove a task by its number:

```bash
python todo.py remove 2
```

### Show Help

Display usage information:

```bash
python todo.py
```

## Data Storage

Tasks are stored in a `tasks.json` file in the same directory as the script. This file is automatically created when you add your first task.

## Examples

```bash
# Add multiple tasks
python todo.py add "Review pull requests"
python todo.py add "Update dependencies"
python todo.py add "Write unit tests"

# Check your tasks
python todo.py list

# Complete a task (remove it)
python todo.py remove 1

# Verify it's gone
python todo.py list
```

## Project Structure

```
.
├── todo.py           # Main application script
├── tasks.json        # Task storage (auto-generated)
├── README.md         # This file
├── LICENSE           # MIT License
├── CONTRIBUTING.md   # Contribution guidelines
└── tests/            # Unit tests
    └── test_todo.py  # Test suite
```

## Development

### Running Tests

```bash
python -m pytest tests/
```

Or with coverage:

```bash
python -m pytest --cov=todo tests/
```

### Code Style

This project follows PEP 8 style guidelines. Format your code using:

```bash
black todo.py
flake8 todo.py
```

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Future Enhancements

Potential features for future releases:

- [ ] Task priorities (high, medium, low)
- [ ] Due dates and reminders
- [ ] Task categories/tags
- [ ] Mark tasks as complete without removing them
- [ ] Search and filter functionality
- [ ] Export tasks to different formats (CSV, Markdown)
- [ ] Colorized output for better visibility
- [ ] Task history and undo functionality

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/codeforgood-org/url-shortener/issues) on GitHub.

## Acknowledgments

- Built with Python standard library only
- Inspired by simple task management needs
- Designed for developers who live in the terminal
