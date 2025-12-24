import pytest
from pages.TodoPage import TodoPage
from utils.data_reader import test_data

# 17
def test_view_all_todos(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("A")
    todo.addTodo("B")
    todo.toggleTodo(1)

    todo.clickAllTab()
    assert todo.getActiveTodoCount() == 1

# 18
def test_all_tab_selected_by_default(page):
    todo = TodoPage(page)
    todo.goto()
    todo.addTodo("Task 1")
    assert todo.isAllTabSelected()

# 19
def test_counter_shows_total_active_items(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Task 1")
    todo.addTodo("Task 2")
    todo.addTodo("Task 3")

    # Mark one task as completed
    todo.toggleTodo(1)

    # Only active items should be counted
    assert todo.getActiveTodoCount() == 2


# 20
def test_filter_shows_only_active_todos(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["addTodo"]["multiple"][0])
    todo.addTodo(test_data["addTodo"]["multiple"][1])
    todo.toggleTodo(1)

    todo.clickActiveTab()

    assert todo.getActiveTodoCount() == 1


# 21
def test_active_todo_counter(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Task 1")
    todo.addTodo("Task 2")
    todo.addTodo("Task 3")

    # Mark one task as completed
    todo.toggleTodo(1)

    # Only active items should be counted
    assert todo.getActiveTodoCount() == 2

# 22
def test_switch_to_active_tab(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Active 1")
    todo.addTodo("Completed 1")
    todo.toggleTodo(1)

    # Switch to Active tab
    todo.clickActiveTab()

    # Verify only active todos are shown
    assert todo.getTotalTodoCount() == 1
    assert todo.getTodoText(0) == "Active 1"



# 23
def test_completed_tab_shows_only_completed(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Completed Task")
    todo.addTodo("Active Task")

    # Mark first todo as completed
    todo.toggleTodo(0)

    # Switch to Completed tab
    todo.clickCompletedTab()

    # Only completed todo should be visible
    assert todo.getTotalTodoCount() == 1
    assert todo.isTodoCompleted(0)

# 24
def test_empty_completed_tab(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Task 1")
    todo.addTodo("Task 2")

    # No task is completed
    todo.clickCompletedTab()

    # Completed tab should be empty
    assert todo.getTotalTodoCount() == 0

# 25
def test_switch_between_tabs(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Task A")
    todo.addTodo("Task B")
    todo.toggleTodo(1)  # Complete second task

    # Active tab
    todo.clickActiveTab()
    # assert todo.getTotalTodoCount() == 1
    assert todo.getTodoText(0) == "Task A"

    # Completed tab
    todo.clickCompletedTab()
    assert todo.getTotalTodoCount() == 1
    assert todo.isTodoCompleted(0)

    # All tab
    todo.clickAllTab()
    assert todo.getTotalTodoCount() == 2






