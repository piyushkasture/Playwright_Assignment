from playwright.sync_api import Page
from pages.BasePage import BasePage


class TodoPage():
    def __init__(self, page:Page):
        self.page = page
        self.base_page = BasePage(page)

        #Locators
        self.todo_input = page.get_by_placeholder("What needs to be done?")
        # self.toggle_checkboxes = page.locator(".toggle")
        self.todo_items = page.get_by_test_id("todo-item")
        self.todo_count = page.locator(".todo-count strong")

        self.all_tab = page.locator(".selected")

        self.active_tab = page.get_by_text("Active")
        self.completed_tab = page.get_by_role("link", name="Completed")
        self.clear_completed_button = page.get_by_text("Clear completed")



    #Methods
    # self.base_pagebase_page.navigate("https://demo.playwright.dev/todomvc/#/")
    def goto(self):
        try:
            self.base_page.navigate("https://demo.playwright.dev/todomvc/#/")
        except Exception as e:
            print(f"Exception while going to website: {e}")
            raise

    def addTodo(self, text):
        try:
            self.todo_input.focus()
            self.todo_input.fill("")
            self.todo_input.fill(text)
            # self.todo_input.press("Enter")
            self.page.keyboard.press("Enter")
        except Exception as e:
            print(f"Exception while adding item: {e}")
            raise

    def toggleTodo(self, index):
        try:
            item = self.todo_items.nth(index)
            checkbox = item.locator(".toggle")
            checkbox.click()

                # Simple stability wait
            self.page.wait_for_timeout(200)
            #
            # checkbox = self.todo_items.nth(index).locator(".toggle")
            # checkbox.check()
        except Exception as e:
            print(f"Exception while toggling item: {e}")
            raise

    def deleteTodo(self, index):
        try:
            itemtToDelete = self.todo_items.nth(index)
            itemtToDelete.hover()
            deleteBtn = itemtToDelete.locator(".destroy")
            deleteBtn.click()
        except Exception as e:
            print(f"Exception while deleting item: {e}")
            raise

    def editTodo(self, index, newText):
        try:
            itemToEdit = self.todo_items.nth(index)
            itemToEdit.dblclick()
            edit_input = itemToEdit.locator(".edit")
            edit_input.fill(newText)
            # edit_input.press("Enter")
            self.page.keyboard.press("Enter")
        except Exception as e:
            print(f"Exception while editing item: {e}")
            raise

    def clickActiveTab(self):
        try:
            self.active_tab.click()
        except Exception as e:
            print(f"Exception while clicking active tab: {e}")
            raise

    def clickCompletedTab(self):
        try:
            self.completed_tab.click()
        except Exception as e:
            print(f"Exception while clicking completed tab: {e}")
            raise

    def clickAllTab(self):
        try:
            self.all_tab.click()
        except Exception as e:
            print(f"Exception while clicking all tab: {e}")
            raise

    def clearCompleted(self):
        try:
            self.clear_completed_button.click()
        except Exception as e:
            print(f"Exception while clearing completed button: {e}")
            raise

    def getActiveTodoCount(self):
        try:
            if self.todo_count.count() == 0:
                return 0
            return int(self.todo_count.inner_text())
        except Exception as e:
            print(f"Exception while Counting active todo: {e}")
            raise

    def getTodoText(self, index):
        try:
            return self.todo_items.nth(index).inner_text()
        except Exception as e:
            print(f"Exception while Todo text: {e}")
            raise

    def isTodoCompleted(self, index):
        try:
            item = self.todo_items.nth(index)
            item.wait_for(timeout=10000)
            classes = item.get_attribute("class")
            return classes is not None and "completed" in classes

        except Exception as e:
            print(f"Exception while checking completed item: {e}")

