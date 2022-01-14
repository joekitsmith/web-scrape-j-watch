import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.web_scraper.data_classes import ContentKeys

from web_scraper.popup import close_popup
from web_scraper.data_classes import Line

from typing import Dict, List


class ContentExtractor:
    def __init__(self, driver: WebDriver) -> None:
        """
        Arguments
        ---------
        driver : WebDriver
            Chrome WebDriver
        """
        self.driver = driver

        # xpaths to elements
        self.xpaths = {
            ContentKeys.TITLE: "//h1[@class='page-title purple']",
            ContentKeys.MAIN_CONTENT: "//div[@class='article-detail__content']",
            ContentKeys.COMMENT_HEADER: "//div[@class='article-detail__comment']/h2",
            ContentKeys.COMMENT_CONTENT: "//div[@class='article-detail__comment']//p",
        }

        # classes of elements
        self.classes = {
            ContentKeys.CONTRIBUTORS: "article-detail__contributors",
            ContentKeys.SUMMARY: "article-detail__precis",
            ContentKeys.LIST: "list",
        }

        self.extracted_content: Dict[str, List[Line]] = {}

    def extract_all_content(self) -> Dict[str, List[Line]]:
        """
        Extract all content from article webpage.

        Returns
        -------
        extracted_content : {str, List[Line]}
            key is section of article
            value is list of Line objects
        """
        close_popup(self.driver)
        time.sleep(1)

        for section_name, xpath in self.xpaths.items():
            try:
                section_elem = WebDriverWait(self.driver, 6).until(
                    EC.visibility_of_element_located((By.XPATH, xpath))
                )
                if section_name == ContentKeys.MAIN_CONTENT:
                    # process main content differently
                    self.get_content_by_class(section_elem)

                else:
                    self.extracted_content[section_name] = Line(section_elem.text)

            except:
                self.extracted_content[section_name] = []

            if section_name not in self.extracted_content:
                self.extracted_content[section_name] = []

        return self.extracted_content

    def get_content_by_class(self, section_elem) -> None:
        """
        Get all content from article where elements are identified using classes.
        Includes contributors, summary and main content.

        Arguments
        ---------
        section_elem :
        """
        contributors = []
        summary = []
        main_content = []

        # get all children of element
        child_elems = section_elem.find_elements(By.XPATH, "./*")
        for child in child_elems:

            # contributors
            if child.get_attribute("class") in self.classes[ContentKeys.CONTRIBUTORS]:
                contributors.append(Line(child.text))

            # summary
            elif child.get_attribute("class") in self.classes[ContentKeys.SUMMARY]:
                summary.append(Line(child.text))

            # main content
            elif child.get_attribute("class") in self.classes[ContentKeys.LIST]:
                list_elems = child.find_elements(By.TAG_NAME, "p")
                for list_elem in list_elems:
                    # add marker for text in list
                    main_content.append(Line(list_elem.text, marker=True))

            else:
                main_content.append(Line(child.text))

        self.extracted_content[ContentKeys.CONTRIBUTORS] = contributors
        self.extracted_content[ContentKeys.SUMMARY] = summary
        self.extracted_content[ContentKeys.MAIN_CONTENT] = main_content
