import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from web_scraper.popup import close_popup


class ContentExtractor:
    def __init__(self, driver):

        self.driver = driver

        self.xpaths = {
            "Title": "//h1[@class='page-title purple']",
            "content": "//div[@class='article-detail__content']",
            "CommentHeader": "//div[@class='article-detail__comment']/h2",
            "CommentContent": "//div[@class='article-detail__comment']//p",
        }

        self.contributor_classes = ["article-detail__contributors"]
        self.summary_classes = ["article-detail__precis"]

        self.text = {}

    def extract_content(self) -> None:
        close_popup(self.driver)

        time.sleep(1)

        for section_name, xpath in self.xpaths.items():
            try:
                section_elem = WebDriverWait(self.driver, 3).until(
                    EC.visibility_of_element_located((By.XPATH, xpath))
                )
                if section_name == "content":
                    self.get_main_body(section_elem)

                else:
                    self.text[section_name] = section_elem.text

            except:
                if section_name == "CommentHeader":
                    self.text["CommentHeader"] = None
                elif section_name == "CommentContent":
                    self.text["CommentContent"] = None

        self.remove_open_in_new_tab()

        return self.text

    def get_main_body(self, section_elem):
        contributors = ""
        main_content = []
        child_elems = section_elem.find_elements(By.XPATH, "./*")
        for child in child_elems:
            if child.get_attribute("class") in self.contributor_classes:
                contributors += child.text
            elif child.get_attribute("class") in self.summary_classes:
                summary = child.text
            else:
                main_content.append(child.text)

        self.text["Contributors"] = contributors
        self.text["Summary"] = summary
        self.text["MainContent"] = main_content

    def remove_open_in_new_tab(self) -> None:
        filtered_text = {}
        for key, value in self.text.items():
            if isinstance(value, str):
                filtered_text[key] = value.replace("\n. opens in new tab\n", ".")
            elif isinstance(value, list):
                filtered_text[key] = [
                    string.replace("\n. opens in new tab\n", ".") for string in value
                ]
            else:
                filtered_text[key] = value

        self.text = filtered_text
