import pytest
from playwright.sync_api import expect
from pages.TodoPage import TodoPage
from utils.data_reader import test_data

# ---------------- TC001 ----------------
def test_add_single_todo_item(page, test_data):
    todo = TodoPage(page)
    todo.goto()
    todo.addTodo(test_data["addTodo"]["single"]["text"])
    assert todo.getActiveTodoCount() == 1
    # expect(todo.getActiveTodoCount()).to_have_count(1)
    # expect(login_page.get_login_error()).to_be_visible(timeout=3000)
#
# ---------------- TC002 ----------------
def test_add_multiple_todo_items(page, test_data):
    todo = TodoPage(page)
    todo.goto()
    for item in test_data["addTodo"]["multiple"]:
        todo.addTodo(item)

    assert todo.getActiveTodoCount() == len(test_data["addTodo"]["multiple"])


# ---------------- TC003 ----------------
def test_add_todo_with_special_character(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    text = test_data["addTodo"]["specialCharacters"]["text"]
    todo.addTodo(text)

    assert todo.getTodoText(0) == text


# ---------------- TC004 ----------------
def test_add_empty_todo(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["addTodo"]["empty"]["text"])
    assert todo.getActiveTodoCount() == 0


# ---------------- TC005 ----------------
def test_add_very_long_todo_text(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["addTodo"]["longText"]["text"])
    assert todo.getActiveTodoCount() == 1


# ---------------- TC006 ----------------
def test_mark_single_todo_complete(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Toggle test")
    todo.toggleTodo(test_data["toggleTodo"]["complete"]["index"])

    assert todo.isTodoCompleted(0)


# ---------------- TC007 ----------------
def test_mark_multiple_todos_complete(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("A")
    todo.addTodo("B")

    todo.toggleTodo(0)
    todo.toggleTodo(1)

    assert todo.isTodoCompleted(0)
    assert todo.isTodoCompleted(1)


# ---------------- TC008 ----------------
def test_unmark_completed_todo(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Unmark")
    todo.toggleTodo(0)
    todo.toggleTodo(0)

    assert not todo.isTodoCompleted(0)


# ---------------- TC009 ----------------
def test_complete_all_todos(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("1")
    todo.addTodo("2")

    todo.toggleTodo(0)
    todo.toggleTodo(1)

    assert todo.getActiveTodoCount() == 0


# ---------------- TC010–TC013 ----------------
def test_edit_todo_text(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["editTodo"]["validEdit"]["original"])
    todo.editTodo(0, test_data["editTodo"]["validEdit"]["updated"])

    assert todo.getTodoText(0) == test_data["editTodo"]["validEdit"]["updated"]


# 11
def test_save_edited_todo(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["editTodo"]["validEdit"]["original"])
    todo.editTodo(0, test_data["editTodo"]["validEdit"]["updated"])

    assert todo.getTodoText(0) == test_data["editTodo"]["validEdit"]["updated"]

# 12
def test_cancel_edit_todo(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    original = test_data["editTodo"]["validEdit"]["original"]
    updated = test_data["editTodo"]["validEdit"]["updated"]

    todo.addTodo(original)
    todo.cancelEditTodo(0, updated)

    assert todo.getTodoText(0) == original

# 13
def test_edit_to_empty_text(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    original = test_data["editTodo"]["validEdit"]["original"]

    todo.addTodo(original)
    todo.editTodo(0, test_data["editTodo"]["emptyEdit"]["updated"])

    # TodoMVC keeps original text if empty edit attempted
    assert todo.getActiveTodoCount() == 0




# ---------------- TC014 ----------------
def test_delete_single_todo(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Delete me")
    todo.deleteTodo(test_data["deleteTodo"]["single"]["index"])

    assert todo.getActiveTodoCount() == 0


# 15
def test_clear_completed_todos(page):
    todo = TodoPage(page)
    todo.goto()

    # Add multiple todos
    todo.addTodo("Task 1")
    todo.addTodo("Task 2")
    todo.addTodo("Task 3")

    # Mark some as completed
    todo.toggleTodo(0)
    todo.toggleTodo(2)

    # Clear completed todos
    todo.clearCompleted()

    # Only active todo should remain
    assert todo.getActiveTodoCount() == 1


# 16
def test_delete_all_todos_individually(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("One")
    todo.addTodo("Two")
    todo.addTodo("Three")

    # Delete todos one by one (always index 0)
    todo.deleteTodo(0)
    todo.deleteTodo(0)
    todo.deleteTodo(0)

    assert todo.getActiveTodoCount() == 0
