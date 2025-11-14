# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub Actions CI/CD workflow with automated testing
- Pre-commit hooks configuration
- Makefile for common development tasks
- Shell completion scripts for bash and zsh
- Security policy documentation
- Code of conduct
- GitHub issue and PR templates

### Changed
- Enhanced CLI with color support
- Added configuration file support

## [1.0.0] - 2025-11-13

### Added
- Complete repository reorganization and enhancement
- Object-oriented design with TodoManager and TodoCLI classes
- Comprehensive README.md with installation and usage instructions
- CONTRIBUTING.md with development guidelines
- Full test suite with 20+ unit tests
- Example scripts (basic and advanced usage)
- pyproject.toml for modern Python project configuration
- requirements.txt for dependency management
- Type hints throughout the codebase
- Comprehensive docstrings for all functions and classes
- Clear command to remove all tasks at once
- Task IDs for better task tracking
- Better error handling and user feedback
- Improved help display with formatted output

### Changed
- Renamed url_shortener.py to todo.py (matches actual functionality)
- Refactored from procedural to object-oriented architecture
- Enhanced validation for all user inputs
- Improved error messages with actionable feedback
- Better file handling with proper encoding and error recovery

### Fixed
- Corrupted JSON file handling
- Empty task validation
- Index out of bounds errors
- File encoding issues with unicode characters

## [0.1.0] - Initial Release

### Added
- Basic todo list functionality
- Add, list, and remove commands
- JSON-based task storage
- Simple command-line interface

---

[Unreleased]: https://github.com/codeforgood-org/url-shortener/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/codeforgood-org/url-shortener/releases/tag/v1.0.0
