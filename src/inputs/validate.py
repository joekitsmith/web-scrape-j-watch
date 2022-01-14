from pathlib import Path
import sys

root_dir = (Path(__file__).parent / "./").resolve()
sys.path.append(str(root_dir))

from datetime import datetime
import validators

from check_response import CheckResponse


def validate_url(url: str) -> CheckResponse:
    """Check if URL input is valid and jwatch.org in URL.

    Arguments
    ---------
    url : str

    Returns
    -------
    check_response : CheckResponse
        True if URL valid
        URL returned if True, otherwise empty string
    """
    if validators.url(url):
        if "jwatch.org" in url:
            return CheckResponse(True, url)

    return CheckResponse(False, "")


def validate_date(date: str) -> CheckResponse:
    """Check date input is valid.

    Arguments
    ---------
    date : str

    Returns
    -------
    check_response : CheckResponse
        True if date valid
        date returned if True, otherwise empty string
    """
    try:
        date_time = datetime.strptime(date, "%m-%Y")
        date_response = (date_time.strftime("%m"), date_time.strftime("%Y"))
        return CheckResponse(True, date_response)

    except:
        return CheckResponse(False, "")
