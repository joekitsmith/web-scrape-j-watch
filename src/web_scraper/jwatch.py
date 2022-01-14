from pathlib import Path
import sys
from typing import Tuple

root_dir = (Path(__file__).parent / "../").resolve()
sys.path.append(str(root_dir))

from web_scraper.configure import ChromeConnection
from web_scraper.login import Login

from web_scraper.change_date import DateChanger
from web_scraper.extract_links import LinkExtractor
from web_scraper.popup import close_popup
from web_scraper.extract_content import ContentExtractor
from web_scraper.data_classes import ContentKeys

from doc_generator.generate_doc import DocumentGenerator


class JWatchScraper:
    def __init__(self, start_url: str, desired_dates: Tuple[str, str, str, str]):
        """
        Arguments
        ---------
        start_url : str
        desired_dates : (str, str, str, str)
            start_month
            start_year
            end_month
            end_year
        """
        self.start_url = start_url
        self.desired_dates = desired_dates

    def scrape(self) -> None:
        """
        Execute functions to extract content and save in docx
        """
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

    def connect(self) -> None:
        """
        Navigate to start URL.
        """
        self.driver = ChromeConnection().driver
        self.driver.get(self.start_url)

    def login(self):
        """ "
        Login to jwatch.org
        """
        Login(self.driver).login()

    def get_paper_content(self) -> None:
        """
        Open article links and save content to document.
        """
        close_popup(self.driver)

        # initialise document
        doc_generator = DocumentGenerator()

        for link in self.article_links:
            try:
                # open article
                self.open_article(link)

                # extract content
                content_extractor = ContentExtractor(self.driver)
                content = content_extractor.extract_all_content()

                # add content to document
                doc_generator.add_page(content)

                print(f"✓ {content[ContentKeys.TITLE].text}")

            except:
                print(f"Unable to extract article: {content[ContentKeys.TITLE].text}")

        # save document
        archive = self.start_url.split("/")[-1]
        start_month, start_year, end_month, end_year = self.desired_dates
        save_name = f"{archive}_{start_month}-{start_year}_to_{end_month}-{end_year}"
        doc_generator.document.save(f"{save_name}.docx")

    def open_article(self, link: str) -> None:
        """
        Arguments
        ---------
        link : str
            navigate link to article
        """
        close_popup(self.driver)

        self.driver.get(link)
