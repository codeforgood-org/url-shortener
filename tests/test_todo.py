"""
Unit tests for the Todo List Manager.

Tests cover the TodoManager and TodoCLI classes to ensure
proper functionality of task management operations.
"""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

# Add parent directory to path to import todo module
sys.path.insert(0, str(Path(__file__).parent.parent))

from todo import TodoManager, TodoCLI


class TestTodoManager(unittest.TestCase):
    """Test cases for the TodoManager class."""

    def setUp(self):
        """Create a temporary file for each test."""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.manager = TodoManager(self.temp_file.name)

    def tearDown(self):
        """Clean up the temporary file after each test."""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)

    def test_load_tasks_empty_file(self):
        """Test loading tasks when file doesn't exist."""
        tasks = self.manager.load_tasks()
        self.assertEqual(tasks, [])

    def test_add_task(self):
        """Test adding a task."""
        result = self.manager.add_task("Test task")
        self.assertTrue(result)

        tasks = self.manager.load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['task'], "Test task")
        self.assertEqual(tasks[0]['id'], 1)

    def test_add_empty_task(self):
        """Test that empty tasks are rejected."""
        result = self.manager.add_task("")
        self.assertFalse(result)

        result = self.manager.add_task("   ")
        self.assertFalse(result)

        tasks = self.manager.load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_add_multiple_tasks(self):
        """Test adding multiple tasks."""
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        self.manager.add_task("Task 3")

        tasks = self.manager.load_tasks()
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0]['task'], "Task 1")
        self.assertEqual(tasks[1]['task'], "Task 2")
        self.assertEqual(tasks[2]['task'], "Task 3")

    def test_remove_task(self):
        """Test removing a task."""
        self.manager.add_task("Task to remove")
        self.manager.add_task("Task to keep")

        result = self.manager.remove_task(1)
        self.assertTrue(result)

        tasks = self.manager.load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['task'], "Task to keep")

    def test_remove_invalid_index(self):
        """Test removing a task with invalid index."""
        self.manager.add_task("Task 1")

        result = self.manager.remove_task(5)
        self.assertFalse(result)

        result = self.manager.remove_task(0)
        self.assertFalse(result)

        tasks = self.manager.load_tasks()
        self.assertEqual(len(tasks), 1)

    def test_remove_from_empty_list(self):
        """Test removing from an empty task list."""
        result = self.manager.remove_task(1)
        self.assertFalse(result)

    def test_clear_all_tasks(self):
        """Test clearing all tasks."""
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        self.manager.add_task("Task 3")

        result = self.manager.clear_all_tasks()
        self.assertTrue(result)

        tasks = self.manager.load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_clear_empty_list(self):
        """Test clearing when list is already empty."""
        result = self.manager.clear_all_tasks()
        self.assertFalse(result)

    def test_task_id_generation(self):
        """Test that task IDs are generated correctly."""
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        self.manager.remove_task(1)
        self.manager.add_task("Task 3")

        tasks = self.manager.load_tasks()
        ids = [task['id'] for task in tasks]

        # IDs should be unique and in ascending order
        self.assertEqual(len(set(ids)), len(ids))
        self.assertEqual(ids, [2, 3])

    def test_load_corrupted_file(self):
        """Test loading a corrupted JSON file."""
        with open(self.temp_file.name, 'w') as f:
            f.write("invalid json{}")

        tasks = self.manager.load_tasks()
        self.assertEqual(tasks, [])

    def test_load_invalid_format(self):
        """Test loading a file with invalid format."""
        with open(self.temp_file.name, 'w') as f:
            json.dump({"invalid": "format"}, f)

        tasks = self.manager.load_tasks()
        self.assertEqual(tasks, [])

    def test_unicode_support(self):
        """Test that unicode characters are supported."""
        self.manager.add_task("测试任务 🎯")

        tasks = self.manager.load_tasks()
        self.assertEqual(tasks[0]['task'], "测试任务 🎯")


class TestTodoCLI(unittest.TestCase):
    """Test cases for the TodoCLI class."""

    def setUp(self):
        """Create a temporary file and CLI instance for each test."""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.manager = TodoManager(self.temp_file.name)
        self.cli = TodoCLI(self.manager)

    def tearDown(self):
        """Clean up the temporary file after each test."""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)

    def test_help_command(self):
        """Test the help command."""
        exit_code = self.cli.run(['help'])
        self.assertEqual(exit_code, 0)

        exit_code = self.cli.run(['-h'])
        self.assertEqual(exit_code, 0)

        exit_code = self.cli.run(['--help'])
        self.assertEqual(exit_code, 0)

    def test_no_arguments(self):
        """Test running with no arguments."""
        exit_code = self.cli.run([])
        self.assertEqual(exit_code, 0)

    def test_add_command(self):
        """Test the add command."""
        exit_code = self.cli.run(['add', 'Test task'])
        self.assertEqual(exit_code, 0)

        tasks = self.manager.load_tasks()
        self.assertEqual(len(tasks), 1)

    def test_add_command_no_description(self):
        """Test add command without description."""
        exit_code = self.cli.run(['add'])
        self.assertEqual(exit_code, 1)

    def test_list_command(self):
        """Test the list command."""
        self.manager.add_task("Task 1")
        exit_code = self.cli.run(['list'])
        self.assertEqual(exit_code, 0)

    def test_remove_command(self):
        """Test the remove command."""
        self.manager.add_task("Task to remove")
        exit_code = self.cli.run(['remove', '1'])
        self.assertEqual(exit_code, 0)

        tasks = self.manager.load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_remove_command_invalid_number(self):
        """Test remove command with invalid number."""
        self.manager.add_task("Task 1")
        exit_code = self.cli.run(['remove', 'abc'])
        self.assertEqual(exit_code, 1)

    def test_remove_command_no_number(self):
        """Test remove command without number."""
        exit_code = self.cli.run(['remove'])
        self.assertEqual(exit_code, 1)

    def test_clear_command(self):
        """Test the clear command."""
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")

        exit_code = self.cli.run(['clear'])
        self.assertEqual(exit_code, 0)

        tasks = self.manager.load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_unknown_command(self):
        """Test an unknown command."""
        exit_code = self.cli.run(['unknown'])
        self.assertEqual(exit_code, 1)

    def test_case_insensitive_commands(self):
        """Test that commands are case-insensitive."""
        exit_code = self.cli.run(['ADD', 'Task 1'])
        self.assertEqual(exit_code, 0)

        exit_code = self.cli.run(['LIST'])
        self.assertEqual(exit_code, 0)


if __name__ == '__main__':
    unittest.main()
