from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from web_scraper.popup import close_popup


class LinkExtractor:
    def __init__(self, driver: WebDriver) -> None:
        """
        Arguments
        ---------
        driver : WebDriver
            Chrome WebDriver
        """
        self.driver = driver

        self.article_links: list = []

    def get_links(self) -> list:
        """
        Extract all links to articles on every page.

        Returns
        -------
        links : List[str]
            links to articles
        """
        print("Extracting links...")

        self.get_paper_links()
        while self.next_page():
            self.get_paper_links()

        return self.article_links

    def get_paper_links(self) -> None:
        """
        Extract links for all articles on single page.
        """
        close_popup(self.driver)

        titles = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "teaser__title"))
        )

        title_link_elems = [title.find_element(By.TAG_NAME, "a") for title in titles]

        self.article_links.extend(
            [title.get_attribute("href") for title in title_link_elems]
        )

    def next_page(self) -> bool:
        """
        Navigate to next page if possible.

        Returns
        -------
        bool
            True if there is a next page, False otherwise
        """
        close_popup(self.driver)
        try:
            next_page_elem = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//i[contains(@class, 'icon icon--fast-forward')]")
                )
            )
            next_page_elem.click()
            return True

        except:
            return False
