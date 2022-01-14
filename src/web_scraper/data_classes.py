from typing import NamedTuple


class ContentKeys:
    TITLE = "title"
    CONTRIBUTORS = "contributors"
    SUMMARY = "summary"
    MAIN_CONTENT = "main_content"
    LIST = "list"
    COMMENT_HEADER = "comment_header"
    COMMENT_CONTENT = "comment_content"


class Line(NamedTuple):
    text: str
    marker: bool = False
