import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://todomvc.com/examples/react/")
    request.cls.driver = driver
    time.sleep(2)

    def teardown():
        driver.quit()

    request.addfinalizer(teardown)


@pytest.mark.usefixtures("setup")
class BaseTest:
    pass


class TestTodoMVC(BaseTest):
    def test_get_todo_mvc_url(self):
        self.driver.find_element_by_class_name("todoapp")

    def test_add_task(self):
        input_field = self.driver.find_element_by_class_name('new-todo')
        input_field.send_keys('task', Keys.ENTER)

        assert self.driver.find_element_by_class_name('todo-list').text == 'task'
        assert self.driver.find_element_by_class_name('todo-count').text == '1 item left'

    def test_deleting_active_todo(self):
        todo = self.driver.find_element_by_class_name('todo-list')
        todo_view = todo.find_element_by_class_name('view')
        destroy_button = todo.find_element_by_class_name('destroy')
        hover = ActionChains(self.driver).move_to_element(todo_view)
        hover.perform()
        if destroy_button.is_displayed():
            destroy_button.click()

        try:
            self.driver.find_element_by_class_name('todo-list').text
        except NoSuchElementException:
            return True

        return False

    def test_edit_task(self):
        self.test_add_task()
        todo = self.driver.find_element_by_class_name('todo-list')
        todo_view = todo.find_element_by_class_name('view')
        todo_edit = todo.find_element_by_class_name('edit')
        ActionChains(self.driver).double_click(todo_view).perform()
        if todo_edit.is_displayed():
            todo_edit.send_keys(" edited", Keys.ENTER)

        assert self.driver.find_element_by_class_name('todo-list').text == 'task edited'

    def test_mark_active_todo_as_complete(self):
        todo = self.driver.find_element_by_class_name('todo-list')
        assert todo.text == 'task edited'

        todo.find_element_by_class_name('toggle').click()

        assert self.driver.find_element_by_class_name('todo-count').text == '0 items left'

    def test_displaying_all_todos(self):
        input_field = self.driver.find_element_by_class_name('new-todo')
        input_field.send_keys('task', Keys.ENTER)

        filters = self.driver.find_element_by_class_name('filters')
        filters.find_element_by_xpath("//li/a[contains(text(), 'All')]").click()
        todos = self.driver.find_element_by_class_name('todo-list')
        active_todos = todos.find_elements_by_xpath("//li[@class='']")
        completed_todos = todos.find_elements_by_xpath("//li[@class='completed']")

        assert len(active_todos) == 1
        assert len(completed_todos) == 1

    def test_mark_completed_todo_as_active(self):
        todo_completed = self.driver.find_element_by_class_name('completed')
        assert todo_completed.text == 'task edited'

        todo_completed.find_element_by_class_name('toggle').click()

        assert self.driver.find_element_by_class_name('todo-count').text == '2 items left'

    def test_displaying_only_active_todos(self):
        filters = self.driver.find_element_by_class_name('filters')
        filters.find_element_by_xpath("//li/a[contains(text(), 'Active')]").click()
        todos = self.driver.find_element_by_class_name('todo-list')
        active_todos = todos.find_elements_by_xpath("//li[@class='']")
        completed_todos = todos.find_elements_by_xpath("//li[@class='completed']")

        assert len(active_todos) == 2
        assert len(completed_todos) == 0

    def test_displaying_only_completed_todos(self):
        todo = self.driver.find_element_by_class_name('todo-list')
        todo.find_element_by_class_name('toggle').click()

        filters = self.driver.find_element_by_class_name('filters')
        filters.find_element_by_xpath("//li/a[contains(text(), 'Completed')]").click()
        todos = self.driver.find_element_by_class_name('todo-list')
        completed_todos = todos.find_elements_by_xpath("//li[@class='completed']")

        assert len(completed_todos) == 1

    def test_deleting_completed_todo(self):
        self.driver.find_element_by_class_name('clear-completed').click()
        todos = self.driver.find_element_by_class_name('todo-list')
        completed_todos = todos.find_elements_by_xpath("//li[@class='completed']")

        assert len(completed_todos) == 0
