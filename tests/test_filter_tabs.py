import pytest
from pages.TodoPage import TodoPage
from utils.data_reader import test_data


def test_all_tab_shows_all(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("A")
    todo.addTodo("B")
    todo.toggleTodo(1)

    todo.clickAllTab()
    assert todo.getActiveTodoCount() == 1

def test_active_tab_filter(page, test_data):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo(test_data["addTodo"]["multiple"][0])
    todo.addTodo(test_data["addTodo"]["multiple"][1])
    todo.toggleTodo(1)

    todo.clickActiveTab()

    assert todo.getActiveTodoCount() == 1


@pytest.mark.regression
def test_completed_tab_shows_completed(page):
    todo = TodoPage(page)
    todo.goto()

    todo.addTodo("Task")
    todo.toggleTodo(0)

    todo.clickCompletedTab()

    assert todo.isTodoCompleted(0)
