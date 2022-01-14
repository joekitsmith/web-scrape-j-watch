from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def close_popup(driver: WebDriver):
    """
    Close popup that appears when navigating jwatch.org.

    Arguments
    ---------
    driver : WebDriver
        Chrome WebDriver
    """
    try:
        popup = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//img[@src="https://siteintercept.qualtrics.com/WRSiteInterceptEngine/../WRQualtricsShared/Graphics/siteintercept/svg-close-btn-black-7.svg"]',
                )
            )
        )
        popup.click()

    except:
        pass
