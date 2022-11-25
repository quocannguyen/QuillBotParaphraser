from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

path_gecko_driver = "C:\\Users\\User\\Downloads\\geckodriver\\geckodriver.exe"
ignored_exceptions = (NoSuchElementException,StaleElementReferenceException,)
timeout = 30


class WebDriverFirefox:
    def __init__(self):
        service = Service(executable_path=path_gecko_driver)
        self.web_driver = Firefox(service=service)

    def click(self, element):
        self.web_driver.execute_script("arguments[0].click()", element)

    def go_to(self, url):
        self.web_driver.get(url)

    def get_by_xpath(self, xpath):
        # return self.web_driver.find_element(By.XPATH, xpath)
        return WebDriverWait(self.web_driver, timeout, ignored_exceptions=ignored_exceptions)\
            .until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
