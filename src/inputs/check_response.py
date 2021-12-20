from typing import NamedTuple


class CheckResponse(NamedTuple):
    valid: bool
    response: str
