#!/usr/bin/env python3
"""
Todo List Manager - A simple command-line task management tool.

This script provides a lightweight interface for managing daily tasks
through the command line. Tasks are persisted to a JSON file.
"""

import json
import os
import sys
from pathlib import Path
from typing import List, Dict, Optional


class Colors:
    """ANSI color codes for terminal output."""

    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

    @classmethod
    def disable(cls) -> None:
        """Disable colors (for non-TTY environments)."""
        cls.RESET = ""
        cls.BOLD = ""
        cls.RED = ""
        cls.GREEN = ""
        cls.YELLOW = ""
        cls.BLUE = ""
        cls.MAGENTA = ""
        cls.CYAN = ""
        cls.WHITE = ""


# Disable colors if not in a TTY environment
if not sys.stdout.isatty():
    Colors.disable()


class Config:
    """Configuration manager for todo list settings."""

    DEFAULT_CONFIG = {
        "tasks_file": "tasks.json",
        "use_colors": True,
        "show_task_ids": True,
        "date_format": "%Y-%m-%d",
    }

    def __init__(self, config_file: str = ".todoconfig.json"):
        """
        Initialize the Config manager.

        Args:
            config_file: Path to the configuration file
        """
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self) -> Dict[str, any]:
        """
        Load configuration from file or use defaults.

        Returns:
            Configuration dictionary
        """
        if not os.path.exists(self.config_file):
            return self.DEFAULT_CONFIG.copy()

        try:
            with open(self.config_file, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                # Merge with defaults
                config = self.DEFAULT_CONFIG.copy()
                config.update(user_config)
                return config
        except (json.JSONDecodeError, Exception):
            return self.DEFAULT_CONFIG.copy()

    def save_config(self) -> bool:
        """
        Save current configuration to file.

        Returns:
            True if successful, False otherwise
        """
        try:
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4)
            return True
        except Exception:
            return False

    def get(self, key: str, default: any = None) -> any:
        """Get a configuration value."""
        return self.config.get(key, default)

    def set(self, key: str, value: any) -> None:
        """Set a configuration value."""
        self.config[key] = value


class TodoManager:
    """Manages todo list operations including CRUD operations on tasks."""

    def __init__(self, tasks_file: str = "tasks.json"):
        """
        Initialize the TodoManager.

        Args:
            tasks_file: Path to the JSON file storing tasks
        """
        self.tasks_file = tasks_file

    def load_tasks(self) -> List[Dict[str, str]]:
        """
        Load tasks from the JSON file.

        Returns:
            List of task dictionaries
        """
        if not os.path.exists(self.tasks_file):
            return []

        try:
            with open(self.tasks_file, "r", encoding="utf-8") as f:
                tasks = json.load(f)
                # Validate that tasks is a list
                if not isinstance(tasks, list):
                    print(f"Warning: {self.tasks_file} format is invalid. Starting fresh.")
                    return []
                return tasks
        except json.JSONDecodeError:
            print(f"Error: {self.tasks_file} is corrupted. Starting fresh.")
            return []
        except Exception as e:
            print(f"Error loading tasks: {e}")
            return []

    def save_tasks(self, tasks: List[Dict[str, str]]) -> bool:
        """
        Save tasks to the JSON file.

        Args:
            tasks: List of task dictionaries to save

        Returns:
            True if successful, False otherwise
        """
        try:
            with open(self.tasks_file, "w", encoding="utf-8") as f:
                json.dump(tasks, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving tasks: {e}")
            return False

    def add_task(self, description: str) -> bool:
        """
        Add a new task to the list.

        Args:
            description: Task description

        Returns:
            True if successful, False otherwise
        """
        if not description or not description.strip():
            print(f"{Colors.RED}Error: Task description cannot be empty.{Colors.RESET}")
            return False

        tasks = self.load_tasks()
        task = {
            "task": description.strip(),
            "id": self._generate_task_id(tasks)
        }
        tasks.append(task)

        if self.save_tasks(tasks):
            print(f"{Colors.GREEN}✓ Added task:{Colors.RESET} {description.strip()}")
            return True
        return False

    def list_tasks(self) -> None:
        """Display all tasks with their numbers."""
        tasks = self.load_tasks()

        if not tasks:
            print(f"{Colors.YELLOW}No tasks found.{Colors.RESET} Add one with: {Colors.CYAN}python todo.py add 'task description'{Colors.RESET}")
            return

        print(f"\n{Colors.BOLD}{Colors.BLUE}You have {len(tasks)} task(s):{Colors.RESET}\n")
        for i, task in enumerate(tasks, 1):
            task_text = task.get('task', 'Unknown task')
            print(f"  {Colors.CYAN}{i}.{Colors.RESET} {task_text}")
        print()

    def remove_task(self, index: int) -> bool:
        """
        Remove a task by its index.

        Args:
            index: 1-based index of the task to remove

        Returns:
            True if successful, False otherwise
        """
        tasks = self.load_tasks()

        if not tasks:
            print(f"{Colors.YELLOW}No tasks to remove.{Colors.RESET}")
            return False

        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            if self.save_tasks(tasks):
                task_text = removed.get('task', 'Unknown task')
                print(f"{Colors.GREEN}✓ Removed task:{Colors.RESET} {task_text}")
                return True
        else:
            print(f"{Colors.RED}Error: Invalid task number. Please choose a number between 1 and {len(tasks)}.{Colors.RESET}")

        return False

    def clear_all_tasks(self) -> bool:
        """
        Remove all tasks from the list.

        Returns:
            True if successful, False otherwise
        """
        tasks = self.load_tasks()

        if not tasks:
            print(f"{Colors.YELLOW}No tasks to clear.{Colors.RESET}")
            return False

        task_count = len(tasks)
        if self.save_tasks([]):
            print(f"{Colors.GREEN}✓ Cleared {task_count} task(s).{Colors.RESET}")
            return True
        return False

    @staticmethod
    def _generate_task_id(tasks: List[Dict[str, str]]) -> int:
        """
        Generate a unique task ID.

        Args:
            tasks: Current list of tasks

        Returns:
            New unique task ID
        """
        if not tasks:
            return 1

        existing_ids = [task.get('id', 0) for task in tasks]
        return max(existing_ids, default=0) + 1


class TodoCLI:
    """Command-line interface for the Todo Manager."""

    def __init__(self, manager: TodoManager):
        """
        Initialize the CLI.

        Args:
            manager: TodoManager instance
        """
        self.manager = manager

    def show_help(self) -> None:
        """Display usage information."""
        help_text = f"""
{Colors.BOLD}{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗
║                  Todo List Manager v1.0                      ║
╚══════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.BOLD}USAGE:{Colors.RESET}
    python todo.py <command> [arguments]

{Colors.BOLD}COMMANDS:{Colors.RESET}
    {Colors.GREEN}add{Colors.RESET} <description>      Add a new task
    {Colors.GREEN}list{Colors.RESET}                   List all tasks
    {Colors.GREEN}remove{Colors.RESET} <number>        Remove a task by number
    {Colors.GREEN}clear{Colors.RESET}                  Remove all tasks
    {Colors.GREEN}config{Colors.RESET} [key] [value]   View or set configuration
    {Colors.GREEN}help{Colors.RESET}                   Show this help message

{Colors.BOLD}EXAMPLES:{Colors.RESET}
    python todo.py add "Buy groceries"
    python todo.py list
    python todo.py remove 1
    python todo.py clear
    python todo.py config
    python todo.py config use_colors false

{Colors.BOLD}For more information, visit:{Colors.RESET}
{Colors.BLUE}https://github.com/codeforgood-org/url-shortener{Colors.RESET}
"""
        print(help_text)

    def run(self, args: List[str]) -> int:
        """
        Execute the CLI with given arguments.

        Args:
            args: Command-line arguments (excluding script name)

        Returns:
            Exit code (0 for success, 1 for error)
        """
        if len(args) < 1:
            self.show_help()
            return 0

        command = args[0].lower()

        if command in ['help', '-h', '--help']:
            self.show_help()
            return 0

        elif command == 'add':
            if len(args) >= 2:
                description = " ".join(args[1:])
                return 0 if self.manager.add_task(description) else 1
            else:
                print("Error: Please provide a task description.")
                print("Usage: python todo.py add 'task description'")
                return 1

        elif command == 'list':
            self.manager.list_tasks()
            return 0

        elif command == 'remove':
            if len(args) == 2:
                try:
                    index = int(args[1])
                    return 0 if self.manager.remove_task(index) else 1
                except ValueError:
                    print("Error: Please provide a valid task number.")
                    return 1
            else:
                print("Error: Please provide a task number to remove.")
                print("Usage: python todo.py remove <number>")
                return 1

        elif command == 'clear':
            return 0 if self.manager.clear_all_tasks() else 1

        elif command == 'config':
            return self.handle_config(args[1:])

        else:
            print(f"{Colors.RED}Error: Unknown command '{command}'{Colors.RESET}")
            self.show_help()
            return 1

    def handle_config(self, args: List[str]) -> int:
        """
        Handle configuration commands.

        Args:
            args: Config command arguments

        Returns:
            Exit code
        """
        config = Config()

        if len(args) == 0:
            # Show all configuration
            print(f"\n{Colors.BOLD}{Colors.BLUE}Current Configuration:{Colors.RESET}\n")
            for key, value in config.config.items():
                print(f"  {Colors.CYAN}{key}:{Colors.RESET} {value}")
            print()
            return 0

        elif len(args) == 1:
            # Show specific config value
            key = args[0]
            value = config.get(key)
            if value is not None:
                print(f"{Colors.CYAN}{key}:{Colors.RESET} {value}")
                return 0
            else:
                print(f"{Colors.RED}Error: Configuration key '{key}' not found.{Colors.RESET}")
                return 1

        elif len(args) == 2:
            # Set config value
            key, value = args[0], args[1]

            # Convert string values to appropriate types
            if value.lower() in ['true', 'false']:
                value = value.lower() == 'true'
            elif value.isdigit():
                value = int(value)

            config.set(key, value)
            if config.save_config():
                print(f"{Colors.GREEN}✓ Configuration updated:{Colors.RESET} {key} = {value}")
                return 0
            else:
                print(f"{Colors.RED}Error: Failed to save configuration.{Colors.RESET}")
                return 1

        else:
            print(f"{Colors.RED}Error: Invalid config command.{Colors.RESET}")
            print("Usage: python todo.py config [key] [value]")
            return 1


def main() -> int:
    """
    Main entry point for the application.

    Returns:
        Exit code
    """
    manager = TodoManager()
    cli = TodoCLI(manager)
    return cli.run(sys.argv[1:])


if __name__ == "__main__":
    sys.exit(main())
