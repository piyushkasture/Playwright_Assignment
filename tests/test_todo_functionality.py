from playwright.sync_api import expect
from utils.data_reader import test_data

# 1
def test_add_single_todo_item(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["addTodo"]["single"]["text"])
    assert todo.getActiveTodoCount() == 1

    expect(todo.todo_input).not_to_be_disabled()
    expect(todo.todo_items.nth(0)).to_have_attribute("data-testid", "todo-item")

# 2
def test_add_multiple_todo_items(website_setup, test_data):
    todo = website_setup

    for item in test_data["addTodo"]["multiple"]:
        todo.addTodo(item)

    assert todo.getActiveTodoCount() == len(test_data["addTodo"]["multiple"])

    for i in range(len(test_data["addTodo"]["multiple"])):
        checkbox = todo.todo_items.nth(i).locator(".toggle")
        expect(checkbox).not_to_be_checked()

# 3
def test_add_todo_with_special_character(website_setup, test_data):
    todo = website_setup

    text = test_data["addTodo"]["specialCharacters"]["text"]
    todo.addTodo(text)

    assert todo.getTodoText(0) == text

# 4
def test_add_empty_todo(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["addTodo"]["empty"]["text"])
    assert todo.getActiveTodoCount() == 0


# 5
def test_add_very_long_todo_text(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["addTodo"]["longText"]["text"])
    assert todo.getActiveTodoCount() == 1


# 6
def test_mark_single_todo_complete(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["addTodo"]["single"]["text"])

    checkbox = todo.todo_items.nth(0).locator(".toggle")
    expect(checkbox).not_to_be_checked()
    
    todo.toggleTodo(test_data["toggleTodo"]["complete"]["index"])

    expect(checkbox).to_be_checked()
    assert todo.isTodoCompleted(0)


# 7
def test_mark_multiple_todos_complete(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["addTodo"]["single"]["text"])
    todo.addTodo(test_data["addTodo"]["single"]["text"])

    todo.toggleTodo(0)
    todo.toggleTodo(1)

    expect(todo.todo_items.nth(0).locator(".toggle")).to_be_checked()
    expect(todo.todo_items.nth(1).locator(".toggle")).to_be_checked()
    assert todo.isTodoCompleted(0)
    assert todo.isTodoCompleted(1)


# 8
def test_unmark_completed_todo(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["addTodo"]["single"]["text"])
    
    checkbox = todo.todo_items.nth(0).locator(".toggle")
    
    todo.toggleTodo(0)
    expect(checkbox).to_be_checked()
    
    todo.toggleTodo(0)
    expect(checkbox).not_to_be_checked()

    assert not todo.isTodoCompleted(0)


# 9
def test_complete_all_todos(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["editTodo"]["validEdit"]["original"])
    todo.addTodo(test_data["editTodo"]["validEdit"]["updated"])

    todo.toggleTodo(0)
    todo.toggleTodo(1)

    assert todo.getActiveTodoCount() == 0


# 10
def test_edit_todo_text(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["editTodo"]["validEdit"]["original"])
    todo.editTodo(0, test_data["editTodo"]["validEdit"]["updatedText"])

    assert todo.getTodoText(0) == test_data["editTodo"]["validEdit"]["updatedText"]


# 11
def test_save_edited_todo(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["editTodo"]["validEdit"]["original"])
    todo.editTodo(0, test_data["editTodo"]["validEdit"]["updated"])

    assert todo.getTodoText(0) == test_data["editTodo"]["validEdit"]["updated"]

# 12
def test_cancel_edit_todo(website_setup, test_data):
    todo = website_setup

    original = test_data["editTodo"]["validEdit"]["original"]
    updated = test_data["editTodo"]["validEdit"]["updated"]

    todo.addTodo(original)
    todo.cancelEditTodo(0, updated)

    assert todo.getTodoText(0) == original

# 13
def test_edit_to_empty_text(website_setup, test_data):
    todo = website_setup

    original = test_data["editTodo"]["validEdit"]["original"]

    todo.addTodo(original)
    todo.editTodo(0, test_data["editTodo"]["emptyEdit"]["updated"])

    assert todo.getActiveTodoCount() == 0

#14
def test_delete_single_todo(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["deleteText"]["text"])
    todo.deleteTodo(test_data["deleteTodo"]["single"]["index"])

    assert todo.getActiveTodoCount() == 0


# 15
def test_clear_completed_todos(website_setup, test_data):
    todo = website_setup

    for item in test_data["addTodo"]["multiple"]:
        todo.addTodo(item)

    todo.toggleTodo(0)
    todo.toggleTodo(2)

    todo.clearCompleted()

    assert todo.getActiveTodoCount() == 1


# 16
def test_delete_all_todos_individually(website_setup, test_data):
    todo = website_setup

    for item in test_data["addTodo"]["multiple"]:
        todo.addTodo(item)

    todo.deleteTodo(0)
    todo.deleteTodo(0)
    todo.deleteTodo(0)

    assert todo.getActiveTodoCount() == 0
