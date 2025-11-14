#!/usr/bin/env python3
"""
Basic usage example for the Todo List Manager.

This example demonstrates how to use the TodoManager class
programmatically in your own Python scripts.
"""

import sys
from pathlib import Path

# Add parent directory to path to import todo module
sys.path.insert(0, str(Path(__file__).parent.parent))

from todo import TodoManager


def main():
    """Demonstrate basic TodoManager usage."""
    # Create a TodoManager instance with a custom file
    manager = TodoManager("example_tasks.json")

    print("=== Todo List Manager - Basic Usage Example ===\n")

    # Add some tasks
    print("Adding tasks...")
    manager.add_task("Write project documentation")
    manager.add_task("Review pull requests")
    manager.add_task("Update dependencies")
    manager.add_task("Run security audit")
    print()

    # List all tasks
    print("Current tasks:")
    manager.list_tasks()

    # Remove a task
    print("Removing task #2...")
    manager.remove_task(2)
    print()

    # List tasks again
    print("Updated task list:")
    manager.list_tasks()

    # Add another task
    print("Adding another task...")
    manager.add_task("Deploy to production")
    print()

    # Final list
    print("Final task list:")
    manager.list_tasks()

    # Clean up example file
    import os
    if os.path.exists("example_tasks.json"):
        os.remove("example_tasks.json")
        print("\nCleaned up example_tasks.json")


if __name__ == "__main__":
    main()
