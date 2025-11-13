#!/usr/bin/env python3
"""
Todo List Manager - A simple command-line task management tool.

This script provides a lightweight interface for managing daily tasks
through the command line. Tasks are persisted to a JSON file.
"""

import json
import os
import sys
from typing import List, Dict, Optional


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
            print("Error: Task description cannot be empty.")
            return False

        tasks = self.load_tasks()
        task = {
            "task": description.strip(),
            "id": self._generate_task_id(tasks)
        }
        tasks.append(task)

        if self.save_tasks(tasks):
            print(f"✓ Added task: {description.strip()}")
            return True
        return False

    def list_tasks(self) -> None:
        """Display all tasks with their numbers."""
        tasks = self.load_tasks()

        if not tasks:
            print("No tasks found. Add one with: python todo.py add 'task description'")
            return

        print(f"\nYou have {len(tasks)} task(s):\n")
        for i, task in enumerate(tasks, 1):
            task_text = task.get('task', 'Unknown task')
            print(f"  {i}. {task_text}")
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
            print("No tasks to remove.")
            return False

        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            if self.save_tasks(tasks):
                task_text = removed.get('task', 'Unknown task')
                print(f"✓ Removed task: {task_text}")
                return True
        else:
            print(f"Error: Invalid task number. Please choose a number between 1 and {len(tasks)}.")

        return False

    def clear_all_tasks(self) -> bool:
        """
        Remove all tasks from the list.

        Returns:
            True if successful, False otherwise
        """
        tasks = self.load_tasks()

        if not tasks:
            print("No tasks to clear.")
            return False

        task_count = len(tasks)
        if self.save_tasks([]):
            print(f"✓ Cleared {task_count} task(s).")
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
        help_text = """
╔══════════════════════════════════════════════════════════════╗
║                  Todo List Manager v1.0                      ║
╚══════════════════════════════════════════════════════════════╝

USAGE:
    python todo.py <command> [arguments]

COMMANDS:
    add <description>      Add a new task
    list                   List all tasks
    remove <number>        Remove a task by number
    clear                  Remove all tasks
    help                   Show this help message

EXAMPLES:
    python todo.py add "Buy groceries"
    python todo.py list
    python todo.py remove 1
    python todo.py clear

For more information, visit:
https://github.com/codeforgood-org/url-shortener
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

        else:
            print(f"Error: Unknown command '{command}'")
            self.show_help()
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
