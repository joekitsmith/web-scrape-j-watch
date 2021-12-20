import os
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class ChromeConnection:
    def __init__(self):

        self.driver = self.configure()

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
            print("exe")
        except Exception:
            base_path = os.path.dirname(__file__)
        print(base_path)
        return os.path.join(base_path, relative_path)

    def configure(self):

        chrome_options = Options()
        chrome_options.headless = True

        # chrome_options.add_argument("user-data-dir=selenium")
        # chrome_options.page_load_strategy = "normal"
        # chrome_options.add_argument("--disable-notifications")

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager(path=self.resource_path("driver")).install()
            )
        )

        return driver
