from selenium.webdriver import ActionChains
import time

class TestDND:
    headless = False

    def test_dnd_papers_to_trash(self, get_driver):
        time.sleep(2)
        trash = get_driver.find_element_by_css_selector('div.trash')
        time.sleep(2)
        docs = get_driver.find_elements_by_css_selector('img.document')
        time.sleep(2)
        for doc in docs:
            ActionChains(get_driver).drag_and_drop(doc, trash).pause(1).perform()
            time.sleep(2)
