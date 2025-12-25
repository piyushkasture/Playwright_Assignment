from pages.TodoPage import TodoPage
from utils.data_reader import test_data

# 1
def test_add_single_todo_item(page, test_data):
    todo = TodoPage(page)
    todo.goto()
    todo.addTodo(test_data["addTodo"]["single"]["text"])
    assert todo.getActiveTodoCount() == 1


# 2
def test_add_multiple_todo_items(page, test_data):
    todo = TodoPage(page)
    todo.goto()
    for item in test_data["addTodo"]["multiple"]:
        todo.addTodo(item)

    assert todo.getActiveTodoCount() == len(test_data["addTodo"]["multiple"])


# 3
def test_add_todo_with_special_character(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    text = test_data["addTodo"]["specialCharacters"]["text"]
    todo.addTodo(text)

    assert todo.getTodoText(0) == text


# 4
def test_add_empty_todo(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["addTodo"]["empty"]["text"])
    assert todo.getActiveTodoCount() == 0


# 5
def test_add_very_long_todo_text(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["addTodo"]["longText"]["text"])
    assert todo.getActiveTodoCount() == 1


# 6
def test_mark_single_todo_complete(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["addTodo"]["single"]["text"])
    todo.toggleTodo(test_data["toggleTodo"]["complete"]["index"])

    assert todo.isTodoCompleted(0)


# 7
def test_mark_multiple_todos_complete(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["addTodo"]["single"]["text"])
    todo.addTodo(test_data["addTodo"]["single"]["text"])

    todo.toggleTodo(0)
    todo.toggleTodo(1)

    assert todo.isTodoCompleted(0)
    assert todo.isTodoCompleted(1)


# 8
def test_unmark_completed_todo(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["addTodo"]["single"]["text"])
    todo.toggleTodo(0)
    todo.toggleTodo(0)

    assert not todo.isTodoCompleted(0)


# 9
def test_complete_all_todos(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["editTodo"]["validEdit"]["original"])
    todo.addTodo(test_data["editTodo"]["validEdit"]["updated"])

    todo.toggleTodo(0)
    todo.toggleTodo(1)

    assert todo.getActiveTodoCount() == 0


# 10
def test_edit_todo_text(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["editTodo"]["validEdit"]["original"])
    todo.editTodo(0, test_data["editTodo"]["validEdit"]["updatedText"])

    assert todo.getTodoText(0) == test_data["editTodo"]["validEdit"]["updatedText"]


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

    assert todo.getActiveTodoCount() == 0

# ---------------- TC014 ----------------
def test_delete_single_todo(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["deleteText"]["text"])
    todo.deleteTodo(test_data["deleteTodo"]["single"]["index"])

    assert todo.getActiveTodoCount() == 0


# 15
def test_clear_completed_todos(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    for item in test_data["addTodo"]["multiple"]:
        todo.addTodo(item)

    todo.toggleTodo(0)
    todo.toggleTodo(2)

    todo.clearCompleted()

    assert todo.getActiveTodoCount() == 1


# 16
def test_delete_all_todos_individually(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    for item in test_data["addTodo"]["multiple"]:
        todo.addTodo(item)

    todo.deleteTodo(0)
    todo.deleteTodo(0)
    todo.deleteTodo(0)

    assert todo.getActiveTodoCount() == 0
