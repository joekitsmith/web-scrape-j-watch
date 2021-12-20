from pathlib import Path
import sys

root_dir = (Path(__file__).parent / "../").resolve()
sys.path.append(str(root_dir))

import time

from web_scraper.configure import ChromeConnection
from web_scraper.login import Login

from web_scraper.change_date import DateChanger
from web_scraper.extract_links import LinkExtractor
from web_scraper.popup import close_popup
from web_scraper.extract_content import ContentExtractor

from doc_generator.generate_doc import DocumentGenerator


class JWatchScraper:
    def __init__(self, start_url, desired_dates):

        self.start_url = start_url
        self.desired_dates = desired_dates

    def scrape(self):
        # connect and log in
        self.connect()
        self.login()

        # set date range
        self.driver.get(self.start_url)
        DateChanger(self.driver).change_date(self.desired_dates)

        # extract all article links
        self.article_links = LinkExtractor(self.driver).get_links()

        # extract content from articles and create documents
        self.get_paper_content()

    def connect(self):
        self.driver = ChromeConnection().driver
        self.driver.get(self.start_url)

    def login(self):
        Login(self.driver).login()

    def get_paper_content(self):
        close_popup(self.driver)

        for link in self.article_links:
            self.open_paper(link)

            content_extractor = ContentExtractor(self.driver)
            content = content_extractor.extract_content()

            doc_generator = DocumentGenerator()
            doc_generator.create_document(content)

    def open_paper(self, link: str) -> None:
        close_popup(self.driver)

        self.driver.get(link)
