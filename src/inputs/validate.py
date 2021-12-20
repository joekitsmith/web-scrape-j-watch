from datetime import datetime
import validators

from .check_response import CheckResponse


def validate_url(url):
    if validators.url(url):
        if "jwatch.org" in url:
            return CheckResponse(True, url)

    return CheckResponse(False, "")


def validate_date(date):
    try:
        date = datetime.strptime(date, "%m-%Y")
        date_response = (date.strftime("%m"), date.strftime("%Y"))
        return CheckResponse(True, date_response)
    except:
        return CheckResponse(False, "")
