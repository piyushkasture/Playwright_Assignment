from playwright.sync_api import expect
from utils.data_reader import test_data


# 26
def test_header_text_and_styling(website_setup,page):
    header = page.locator("header h1")

    expect(header).to_have_text("todos")
    expect(header).to_be_visible()

    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
    expect(page).to_have_title("React • TodoMVC")


# 27
def test_input_placeholder_text(website_setup, test_data):
    todo = website_setup

    expect(todo.todo_input).to_have_attribute("placeholder", test_data["uiValidation"]["placeholderText"])

    expect(todo.todo_input).not_to_be_disabled()

# 28
def test_footer_visibility_rules(website_setup,page):
    todo = website_setup

    footer = page.locator("footer.footer")
    expect(footer).not_to_be_visible()

    todo.addTodo("Task 1")
    expect(footer).to_be_visible()

    expect(footer).to_have_attribute("class", "footer")

    expect(footer).to_have_css("display", "block")


# 29
def test_clear_completed_button(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["addTodo"]["multiple"][0])
    todo.toggleTodo(0)

    expect(todo.clear_completed_button).to_be_visible()
    expect(todo.clear_completed_button).not_to_be_disabled()
    expect(todo.clear_completed_button).to_have_text("Clear completed")
# 30
def test_checkbox_interaction(website_setup,test_data):
    todo = website_setup

    todo.addTodo(test_data["addTodo"]["multiple"][1])

    checkbox = todo.todo_items.nth(0).locator(".toggle")
    expect(checkbox).not_to_be_checked()

    todo.toggleTodo(0)

    expect(checkbox).to_be_checked()
    assert todo.isTodoCompleted(0)

# 31
def test_hover_effect_delete_button(website_setup,test_data):
    todo = website_setup

    todo.addTodo(test_data["deleteText"]["deleteHover"])

    item = todo.todo_items.nth(0)
    delete_button = item.locator(".destroy")

    item.hover()
    expect(delete_button).to_be_visible()
    expect(delete_button).not_to_be_disabled()

# 32
def test_tab_navigation(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["addTodo"]["single"]["text"])

    todo.todo_input.focus()
    expect(todo.todo_input).to_be_focused()
    expect(todo.all_tab).to_be_visible()
    expect(todo.all_tab).to_have_attribute("href", "#/")


# 33
def test_input_field_behavior(website_setup,page):
    todo = website_setup

    todo.todo_input.focus()
    expect(todo.todo_input).to_be_focused()
    expect(todo.todo_input).not_to_be_disabled()

    page.locator("header h1").click()
    expect(todo.todo_input).not_to_be_focused()
