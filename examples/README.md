# Examples

This directory contains example scripts demonstrating how to use the Todo List Manager.

## Basic Usage Example

**File:** `basic_usage.py`

Demonstrates the fundamental operations of the TodoManager:
- Creating a TodoManager instance
- Adding tasks
- Listing tasks
- Removing tasks

**Run it:**
```bash
python examples/basic_usage.py
```

## Advanced Usage Example

**File:** `advanced_usage.py`

Shows how to extend the TodoManager class with custom features:
- Adding priority levels to tasks
- Organizing tasks by priority
- Adding timestamps
- Getting task statistics

**Run it:**
```bash
python examples/advanced_usage.py
```

## Creating Your Own Extensions

The TodoManager class is designed to be easily extensible. Here's a simple pattern:

```python
from todo import TodoManager

class MyCustomTodoManager(TodoManager):
    """Add your custom features here."""

    def my_custom_method(self):
        """Implement your custom functionality."""
        tasks = self.load_tasks()
        # Your custom logic here
        self.save_tasks(tasks)

# Use it
manager = MyCustomTodoManager()
manager.add_task("My task")
manager.my_custom_method()
```

## Ideas for Extensions

Here are some ideas you could implement:

1. **Tags/Categories**: Add tags to tasks for better organization
2. **Due Dates**: Track when tasks are due
3. **Recurring Tasks**: Tasks that repeat on a schedule
4. **Task Dependencies**: Tasks that depend on other tasks
5. **Sub-tasks**: Break down tasks into smaller steps
6. **Time Tracking**: Track time spent on tasks
7. **Task Notes**: Add detailed notes to tasks
8. **Search/Filter**: Search tasks by keywords or filters
9. **Export/Import**: Export tasks to CSV, JSON, or other formats
10. **Notifications**: Get reminders for due tasks
