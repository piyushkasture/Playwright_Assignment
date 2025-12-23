import pytest
from playwright.sync_api import expect
from pages.TodoPage import TodoPage
from utils.data_reader import test_data

# ---------------- TC001 ----------------
def test_add_single_todo(page, test_data):
    todo = TodoPage(page)
    todo.goto()
    todo.addTodo(test_data["addTodo"]["single"]["text"])
    assert todo.getActiveTodoCount() == 1
    # expect(todo.getActiveTodoCount()).to_have_count(1)
    # expect(login_page.get_login_error()).to_be_visible(timeout=3000)
#
# ---------------- TC002 ----------------
def test_add_multiple_todos(page, test_data):
    todo = TodoPage(page)
    todo.goto()
    for item in test_data["addTodo"]["multiple"]:
        todo.addTodo(item)

    assert todo.getActiveTodoCount() == len(test_data["addTodo"]["multiple"])


# ---------------- TC003 ----------------
def test_add_special_character_todo(page, test_data):
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
def test_add_long_text_todo(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["addTodo"]["longText"]["text"])
    assert todo.getActiveTodoCount() == 1


# ---------------- TC006 ----------------
def test_toggle_todo_complete(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Toggle test")
    todo.toggleTodo(test_data["toggleTodo"]["complete"]["index"])

    assert todo.isTodoCompleted(0)


# ---------------- TC007 ----------------
def test_toggle_multiple_todos(page):
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
def test_edit_todo_valid(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["editTodo"]["validEdit"]["original"])
    todo.editTodo(0, test_data["editTodo"]["validEdit"]["updated"])

    assert todo.getTodoText(0) == test_data["editTodo"]["validEdit"]["updated"]


# ---------------- TC014 ----------------
def test_delete_single_todo(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Delete me")
    todo.deleteTodo(test_data["deleteTodo"]["single"]["index"])

    assert todo.getActiveTodoCount() == 0
