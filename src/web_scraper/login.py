import json
import time
import pathlib

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Config:
    def __init__(self) -> None:
        self.get_config()

    def get_config(self) -> None:
        """
        Get email and password from json config file.
        json file must be stored in same directory as this file.
        """
        root_dir = pathlib.Path(__file__).parent.resolve()
        with open(f"{root_dir}/config.json") as f:
            config = json.load(f)
            self.email = config["Email"]
            self.password = config["Password"]


class Login:
    def __init__(self, driver: WebDriver) -> None:
        """
        Arguments
        ---------
        driver : WebDriver
            Chrome Webdriver
        """
        self.driver = driver
        self.config = Config()

    def login(self) -> None:
        """
        Execute functions to login.
        """
        print("Logging in...")

        self.click_login_header()
        self.enter_details()
        self.click_sign_in()

    def click_login_header(self) -> None:
        """
        Click login button in header to begin login procedure.
        """
        login_header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "signin-header"))
        )
        login_header.click()

    def enter_details(self) -> None:
        """
        Add email and password information into input fields.
        """
        input_fields = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "app-login-page"))
        )

        email = input_fields.find_element(By.ID, "email_text")
        email.send_keys(self.config.email)

        password = input_fields.find_element(By.ID, "pwd_text")
        password.send_keys(self.config.password)

    def click_sign_in(self) -> None:
        """
        Click sign in button.
        """
        sign_in = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/app-root/div/app-login-page/div/div[1]/login/form/div/div/div/div[4]/button",
                )
            )
        )
        sign_in.click()

        # wait for sign in to occur
        time.sleep(5)
