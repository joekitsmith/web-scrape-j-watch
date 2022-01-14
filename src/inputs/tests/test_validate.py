import io
from pathlib import Path
import sys

root_dir = (Path(__file__).parent / "../").resolve()
sys.path.append(str(root_dir))

from check_response import CheckResponse
from validate import validate_url, validate_date


class TestValidateURL:
    def test_validate_url_validURL(self):
        # assemble
        url = "https://www.jwatch.org/general-medicine-online-archives"
        # act
        url_check = validate_url(url)
        # assert
        assert url_check == CheckResponse(
            True, "https://www.jwatch.org/general-medicine-online-archives"
        )

    def test_validate_url_invalidURL(self):
        # assemble
        url = "invalid_url"
        # act
        url_check = validate_url(url)
        # assert
        assert url_check == CheckResponse(False, "")

    def test_validate_url_validURL_jwatchNotInURL(self):
        # assemble
        url = "https://www.google.com/"
        # act
        url_check = validate_url(url)
        # assert
        assert url_check == CheckResponse(False, "")


class TestValidateDate:
    def test_validate_date_validDate(self):
        # assemble
        date = "02-2021"
        # act
        date_check = validate_date(date)
        # assert
        assert date_check == CheckResponse(True, ("02", "2021"))

    def test_validate_date_dateIncludesDay(self):
        # assemble
        date = "01-02-2021"
        # act
        date_check = validate_date(date)
        # assert
        assert date_check == CheckResponse(False, "")

    def test_validate_date_monthNotValid(self):
        # assemble
        date = "13-2021"
        # act
        date_check = validate_date(date)
        # assert
        assert date_check == CheckResponse(False, "")

    def test_validate_date_noHyphen(self):
        # assemble
        date = "13/2021"
        # act
        date_check = validate_date(date)
        # assert
        assert date_check == CheckResponse(False, "")

    def test_validate_date_twoDigitYear(self):
        # assemble
        date = "13-21"
        # act
        date_check = validate_date(date)
        # assert
        assert date_check == CheckResponse(False, "")
