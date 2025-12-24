from playwright.sync_api import expect
from pages.TodoPage import TodoPage
from utils.data_reader import test_data


# 26
def test_header_text_and_styling(page):
    todo = TodoPage(page)
    todo.goto()

    header = page.locator("header h1")

    expect(header).to_have_text("todos")
    expect(header).to_be_visible()


# 27
def test_input_placeholder_text(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    expect(todo.todo_input).to_have_attribute(
        "placeholder",
        test_data["uiValidation"]["placeholderText"]
    )

# 28
def test_footer_visibility_rules(page):
    todo = TodoPage(page)
    todo.goto()

    footer = page.locator("footer.footer")

    # Todo footer hidden initially
    expect(footer).not_to_be_visible()

    todo.addTodo("Task 1")

    # Todo footer visible after adding todo
    expect(footer).to_be_visible()


# 29
def test_clear_completed_button(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Task 1")
    todo.toggleTodo(0)

    expect(todo.clear_completed_button).to_be_visible()

# 30
def test_checkbox_interaction(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Task 1")

    # Click checkbox
    todo.toggleTodo(0)

    # Completed class should be applied
    assert todo.isTodoCompleted(0)

# 31
def test_hover_effect_delete_button(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Hover Task")

    item = todo.todo_items.nth(0)
    delete_button = item.locator(".destroy")

    # Hover over todo item
    item.hover()

    # Delete (X) button should be visible
    expect(delete_button).to_be_visible()

# 32
def test_tab_navigation(page):
    todo = TodoPage(page)
    todo.goto()

    # Input should be focusable
    todo.todo_input.focus()
    expect(todo.todo_input).to_be_focused()


# 33
def test_input_field_behavior(page):
    todo = TodoPage(page)
    todo.goto()

    # Focus input
    todo.todo_input.focus()
    expect(todo.todo_input).to_be_focused()

    # Blur input by clicking elsewhere
    page.locator("header h1").click()
    expect(todo.todo_input).not_to_be_focused()
