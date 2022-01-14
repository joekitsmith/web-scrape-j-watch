import os
import sys

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def resource_path(relative_path: str) -> str:
    """Get path to file if running from .exe or from .py

    Arguments
    ---------
    relative_path : str

    Returns
    -------
    resource_path : str
    """
    try:
        base_path = sys._MEIPASS  # type: ignore
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


class ChromeConnection:
    def __init__(self) -> None:

        self.driver = self.configure()

    def configure(self) -> WebDriver:
        """
        Configure Chromedriver settings.

        Returns
        ---------
        driver : Webdriver
            Chrome WebDriver initialised with custom settings
        """
        chrome_options = Options()
        # no warnings
        chrome_options.add_argument("log-level=3")
        # no browser
        chrome_options.add_argument("--headless")

        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")

        # create driver with variable path depending on run location of .exe or .py
        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager(path=resource_path("driver")).install()
            ),
            options=chrome_options,
        )

        return driver
