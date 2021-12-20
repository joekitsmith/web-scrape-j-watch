from pathlib import Path
import sys

root_dir = (Path(__file__).parent / "../").resolve()
sys.path.append(str(root_dir))

from web_scraper.configure import ChromeConnection


class JWatchScraper:
    def __init__(self, start_url, desired_dates):

        self.start_url = start_url
        self.desired_dates = desired_dates

    def scrape(self):
        # connect and log in
        self.connect()

    def connect(self):
        self.driver = ChromeConnection().driver
        self.driver.get(self.start_url)

