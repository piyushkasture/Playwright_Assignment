from playwright.sync_api import expect
from pages.TodoPage import TodoPage
from utils.data_reader import test_data


def test_input_placeholder_text(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    expect(todo.todo_input).to_have_attribute(
        "placeholder",
        test_data["uiValidation"]["placeholderText"]
    )



def test_clear_completed_visible(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Task")
    todo.toggleTodo(0)

    expect(todo.clear_completed_button).to_be_visible()

