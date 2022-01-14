from typing import Tuple
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select

from web_scraper.popup import close_popup


class DateChanger:
    def __init__(self, driver) -> None:

        self.driver = driver

    def change_date(self, desired_dates: Tuple[str, str, str, str]) -> None:
        """Find date elements on page and enter desired dates.
        Find submit button and click submit.

        Arguments
        ---------
        desired_dates : (str, str, str, str)
            start_month
            start_year
            end_month
            end_year
        """
        close_popup(self.driver)

        # get drop-down date selector element
        all_dates = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(
                (
                    By.XPATH,
                    "//select[contains(@class, 'dropdown-select ng-untouched ng-pristine ng-valid')]",
                )
            )
        )
        for i, date_elem in enumerate(all_dates):
            select = Select(date_elem)
            if i % 2 == 0:
                # month element
                select.select_by_value(desired_dates[i])
                # year element
            else:
                select.select_by_visible_text(desired_dates[i])

        # submit button
        submit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//i[contains(@class, 'icon icon--submit')]")
            )
        )
        submit.click()
