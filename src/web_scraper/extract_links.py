from tqdm import tqdm

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from web_scraper.popup import close_popup


class LinkExtractor:
    def __init__(self, driver):

        self.driver = driver

        self.article_links = []

    def get_links(self) -> list:
        print("Extracting links...")

        self.get_paper_links()
        while self.next_page():
            self.get_paper_links()

        return self.article_links

    def get_paper_links(self):
        close_popup(self.driver)

        titles = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "teaser__title"))
        )

        title_link_elems = [title.find_element(By.TAG_NAME, "a") for title in titles]

        self.article_links.extend(
            [title.get_attribute("href") for title in title_link_elems]
        )

    def next_page(self):
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
