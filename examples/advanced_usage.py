#!/usr/bin/env python3
"""
Advanced usage example for the Todo List Manager.

This example shows how to extend the TodoManager class
and add custom functionality.
"""

import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict

# Add parent directory to path to import todo module
sys.path.insert(0, str(Path(__file__).parent.parent))

from todo import TodoManager


class AdvancedTodoManager(TodoManager):
    """Extended TodoManager with additional features."""

    def add_task_with_priority(self, description: str, priority: str = "medium") -> bool:
        """
        Add a task with a priority level.

        Args:
            description: Task description
            priority: Priority level (high, medium, low)

        Returns:
            True if successful, False otherwise
        """
        if priority not in ["high", "medium", "low"]:
            print(f"Error: Invalid priority '{priority}'. Use high, medium, or low.")
            return False

        tasks = self.load_tasks()
        task = {
            "task": description.strip(),
            "id": self._generate_task_id(tasks),
            "priority": priority,
            "created_at": datetime.now().isoformat()
        }
        tasks.append(task)

        if self.save_tasks(tasks):
            print(f"✓ Added {priority} priority task: {description.strip()}")
            return True
        return False

    def list_tasks_by_priority(self) -> None:
        """Display tasks organized by priority."""
        tasks = self.load_tasks()

        if not tasks:
            print("No tasks found.")
            return

        priority_order = ["high", "medium", "low", None]
        priority_labels = {
            "high": "🔴 HIGH PRIORITY",
            "medium": "🟡 MEDIUM PRIORITY",
            "low": "🟢 LOW PRIORITY",
            None: "⚪ NO PRIORITY"
        }

        print(f"\nYou have {len(tasks)} task(s):\n")

        for priority in priority_order:
            priority_tasks = [t for t in tasks if t.get('priority') == priority]

            if priority_tasks:
                print(f"{priority_labels[priority]}:")
                for task in priority_tasks:
                    task_id = tasks.index(task) + 1
                    task_text = task.get('task', 'Unknown task')
                    created = task.get('created_at', 'Unknown')
                    if created != 'Unknown':
                        created = created.split('T')[0]
                    print(f"  {task_id}. {task_text} (created: {created})")
                print()

    def get_task_count_by_priority(self) -> Dict[str, int]:
        """Get count of tasks by priority level."""
        tasks = self.load_tasks()
        counts = {"high": 0, "medium": 0, "low": 0, "none": 0}

        for task in tasks:
            priority = task.get('priority', 'none')
            if priority in counts:
                counts[priority] += 1
            else:
                counts['none'] += 1

        return counts


def main():
    """Demonstrate advanced TodoManager usage."""
    # Create an AdvancedTodoManager instance
    manager = AdvancedTodoManager("advanced_tasks.json")

    print("=== Todo List Manager - Advanced Usage Example ===\n")

    # Add tasks with priorities
    print("Adding tasks with priorities...")
    manager.add_task_with_priority("Fix critical security bug", "high")
    manager.add_task_with_priority("Update documentation", "low")
    manager.add_task_with_priority("Implement new feature", "medium")
    manager.add_task_with_priority("Review code", "medium")
    manager.add_task_with_priority("Deploy hotfix", "high")
    print()

    # List tasks by priority
    print("Tasks organized by priority:")
    manager.list_tasks_by_priority()

    # Get task statistics
    counts = manager.get_task_count_by_priority()
    print("Task Statistics:")
    print(f"  High priority: {counts['high']}")
    print(f"  Medium priority: {counts['medium']}")
    print(f"  Low priority: {counts['low']}")
    print(f"  No priority: {counts['none']}")
    print()

    # Remove a task
    print("Completing task #1...")
    manager.remove_task(1)
    print()

    # Show updated list
    print("Updated task list:")
    manager.list_tasks_by_priority()

    # Clean up example file
    import os
    if os.path.exists("advanced_tasks.json"):
        os.remove("advanced_tasks.json")
        print("\nCleaned up advanced_tasks.json")


if __name__ == "__main__":
    main()
