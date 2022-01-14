from web_scraper.jwatch import JWatchScraper
from inputs.get_inputs import get_inputs

default_url = "https://www.jwatch.org/general-medicine-online-archives"
default_dates = ("02", "2021", "12", "2021")

if __name__ == "__main__":
    url, dates = get_inputs()
    JWatchScraper(url, dates).scrape()
