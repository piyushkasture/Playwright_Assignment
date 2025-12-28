from utils.data_reader import test_data

# 17
def test_view_all_todos(website_setup,test_data):
    todo = website_setup

    todo.addTodo(test_data["addTodo"]["single"]["text"])
    todo.addTodo(test_data["tabs"]["active"])
    todo.toggleTodo(1)

    todo.clickAllTab()
    assert todo.getActiveTodoCount() == 1

# 18
def test_all_tab_selected_by_default(website_setup, test_data):
    todo = website_setup
    todo.addTodo(test_data["addTodo"]["single"]["text"])
    assert todo.isAllTabSelected()

# 19
def test_counter_shows_total_active_items(website_setup, test_data):
    todo = website_setup

    for item in test_data["addTodo"]["multiple"]:
        todo.addTodo(item)

    todo.toggleTodo(1)

    assert todo.getActiveTodoCount() == 2


# 20
def test_filter_shows_only_active_todos(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["addTodo"]["multiple"][1])
    todo.addTodo(test_data["addTodo"]["multiple"][2])
    todo.toggleTodo(1)

    todo.clickActiveTab()

    assert todo.getActiveTodoCount() == 1


# 21
def test_active_todo_counter(website_setup, test_data):
    todo = website_setup

    for item in test_data["addTodo"]["multiple"]:
        todo.addTodo(item)

    todo.toggleTodo(1)

    assert todo.getActiveTodoCount() == 2

# 22
def test_switch_to_active_tab(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["tabs"]["active"])
    todo.addTodo(test_data["tabs"]["complete"])
    todo.toggleTodo(1)

    todo.clickActiveTab()

    assert todo.getTotalTodoCount() == 1
    assert todo.getTodoText(0) == "Active Task"

# 23
def test_completed_tab_shows_only_completed(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["tabs"]["complete"])
    todo.addTodo(test_data["tabs"]["active"])

    todo.toggleTodo(0)

    todo.clickCompletedTab()

    assert todo.getTotalTodoCount() == 1
    assert todo.isTodoCompleted(0)

# 24
def test_empty_completed_tab(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["addTodo"]["multiple"][0])
    todo.addTodo(test_data["addTodo"]["multiple"][1])

    todo.clickCompletedTab()

    assert todo.getTotalTodoCount() == 0

# 25
def test_switch_between_tabs(website_setup, test_data):
    todo = website_setup

    todo.addTodo(test_data["addTodo"]["multiple"][0])
    todo.addTodo(test_data["addTodo"]["multiple"][1])
    todo.toggleTodo(1)

    todo.clickActiveTab()

    assert todo.getTodoText(0) == "Task 1"

    todo.clickCompletedTab()
    assert todo.getTotalTodoCount() == 1
    assert todo.isTodoCompleted(0)

    todo.clickAllTab()
    assert todo.getTotalTodoCount() == 2






