from pathlib import Path
import sys

root_dir = (Path(__file__).parent / "./").resolve()
sys.path.append(str(root_dir))

from typing import Tuple
from validate import validate_url, validate_date


def get_inputs() -> Tuple[str, str]:
    """
    Request inputs start user for URL and date range.

    Returns
    -------
    url : str
    dates : str
    """
    url = get_url()

    start_date = get_start_date()
    end_date = get_end_date()
    dates = start_date + end_date

    return (url, dates)


def get_url() -> str:
    """
    Request URL input start user.

    Returns
    -------
    url : str
    """
    url_check = validate_url(input("Enter jwatch.org archive url: "))

    if not url_check.valid:
        print("URL not valid")
        return get_url()

    else:
        return url_check.response


def get_start_date():
    """
    Request start date from user.

    Returns
    -------
    start_date : str
    """
    start_date_check = validate_date(input("Enter start date with format MM-YYYY: "))
    if not start_date_check.valid:
        print("Start date not valid")
        return get_start_date()
    else:
        return start_date_check.response


def get_end_date():
    """
    Request end date from user.

    Returns
    -------
    end_date : str
    """
    end_date_check = validate_date(input("Enter end date with format MM-YYYY: "))

    if not end_date_check.valid:
        print("End date not valid")
        return get_end_date()

    else:
        return end_date_check.response
