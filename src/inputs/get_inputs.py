from .validate import validate_url, validate_date


def get_inputs():
    url = get_url()
    from_date = get_from_date()
    to_date = get_to_date()
    dates = from_date + to_date
    return (url, dates)


def get_url():
    url_check = validate_url(input("Enter jwatch.org url: "))
    if not url_check.valid:
        print("URL not valid")
        return get_url()
    else:
        return url_check.response


def get_from_date():
    from_date_check = validate_date(input("Enter start date with format MM-YYYY: "))
    if not from_date_check.valid:
        print("Start date not valid")
        return get_from_date()
    else:
        return from_date_check.response


def get_to_date():
    to_date_check = validate_date(input("Enter end date with format MM-YYYY: "))
    if not to_date_check.valid:
        print("End date not valid")
        return get_to_date()
    else:
        return to_date_check.response
