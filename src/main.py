from web_scraper.jwatch import JWatchScraper
from inputs.get_inputs import get_inputs

backup_url = "https://www.jwatch.org/general-medicine-online-archives"
backup_dates = ["Feb", "2021", "Dec", "2021"]

if __name__ == "__main__":
    url, dates = get_inputs()
    JWatchScraper(url, dates).scrape()