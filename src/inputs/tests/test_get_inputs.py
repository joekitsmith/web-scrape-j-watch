import io
from pathlib import Path
import sys

root_dir = (Path(__file__).parent / "../").resolve()
sys.path.append(str(root_dir))

from check_response import CheckResponse
from get_inputs import get_inputs, get_url, get_start_date, get_end_date


class TestGetInputs:
    def test_get_inputs(self, mocker):
        # assemble
        mocker.patch(
            "get_inputs.get_url",
            return_value="https://www.jwatch.org/general-medicine-online-archives",
        )
        mocker.patch("get_inputs.get_start_date", return_value=("02", "2021"))
        mocker.patch("get_inputs.get_end_date", return_value=("03", "2021"))
        # act
        url, dates = get_inputs()
        # assert
        assert url == "https://www.jwatch.org/general-medicine-online-archives"
        assert dates == ("02", "2021", "03", "2021")


class TestGetURL:
    def test_get_url_urlValid(self, mocker):
        # assemble
        mocker.patch(
            "get_inputs.validate_url",
            return_value=CheckResponse(
                True, "https://www.jwatch.org/general-medicine-online-archives"
            ),
        )
        mocker.patch("builtins.input", return_value="")
        # act
        url = get_url()
        assert url == "https://www.jwatch.org/general-medicine-online-archives"

    def test_get_url_urlInitiallyInvalid(self, mocker):
        # assemble
        mocker.patch(
            "get_inputs.validate_url",
            side_effect=[
                CheckResponse(False, ""),
                CheckResponse(
                    True, "https://www.jwatch.org/general-medicine-online-archives"
                ),
            ],
        )
        mocker.patch("builtins.input", return_value="")
        # act
        with mocker.patch("sys.stdout", new=io.StringIO()) as std_out:
            url = get_url()
            assert std_out.getvalue() == "URL not valid\n"
            assert url == "https://www.jwatch.org/general-medicine-online-archives"


class TestGetStartDate:
    def test_get_start_date_startDateValid(self, mocker):
        # assemble
        mocker.patch(
            "get_inputs.validate_date",
            return_value=CheckResponse(True, ("02", "2021")),
        )
        mocker.patch("builtins.input", return_value="")
        # act
        start_date = get_start_date()
        assert start_date == ("02", "2021")

    def test_get_start_date_startDateInitiallyInvalid(self, mocker):
        # assemble
        mocker.patch(
            "get_inputs.validate_date",
            side_effect=[
                CheckResponse(False, ""),
                CheckResponse(True, ("02", "2021")),
            ],
        )
        mocker.patch("builtins.input", return_value="")
        # act
        with mocker.patch("sys.stdout", new=io.StringIO()) as std_out:
            start_date = get_start_date()
            assert std_out.getvalue() == "Start date not valid\n"
            assert start_date == ("02", "2021")


class TestGetEndDate:
    def test_get_end_date_endDateValid(self, mocker):
        # assemble
        mocker.patch(
            "get_inputs.validate_date",
            return_value=CheckResponse(True, ("03", "2021")),
        )
        mocker.patch("builtins.input", return_value="")
        # act
        end_date = get_end_date()
        assert end_date == ("03", "2021")

    def test_get_end_date_endDateInitiallyInvalid(self, mocker):
        # assemble
        mocker.patch(
            "get_inputs.validate_date",
            side_effect=[
                CheckResponse(False, ""),
                CheckResponse(True, ("03", "2021")),
            ],
        )
        mocker.patch("builtins.input", return_value="")
        # act
        with mocker.patch("sys.stdout", new=io.StringIO()) as std_out:
            end_date = get_end_date()
            assert std_out.getvalue() == "End date not valid\n"
            assert end_date == ("03", "2021")
