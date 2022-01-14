from pathlib import Path
import sys

root_dir = (Path(__file__).parent / "../").resolve()
sys.path.append(str(root_dir))

from typing import List
from web_scraper.data_classes import Line


def clean_text(text: List[Line]) -> str:
    """
    Remove unwanted sub-string and add line breaks for all extracted text.

    Arguments
    ---------
    extracted_text : {str, List[Line]}
        keys are sections of article
        values are list of Line objects containing text from section

    Returns
    -------
    cleaned_text : {str, List[Line]}
        values have sub-string removed and line breaks between lines
    """
    return add_line_breaks(remove_open_in_new_tab(text))


def remove_open_in_new_tab(value: List[Line]) -> List[Line]:
    """
    For every line of text in extracted_content, remove 'opens in new tab' sub-strings
    """
    list_text = []

    if isinstance(value, list):
        for line in value:
            # replace sub-string in text and retain marker property
            filtered_string = Line(
                line.text.replace("\n. opens in new tab\n", "."),
                line.marker,
            )
            list_text.append(filtered_string)

    return list_text


def add_line_breaks(content: List[Line]) -> str:
    """Add line breaks between text of Line objects in single string.

    Arguments
    ----------
    content : list
        list of Line objects

    Returns
    -------
    content_string : str
        single string with lines separated by new-line characters
    """
    content_string = ""
    if isinstance(content, list):
        for i, line in enumerate(content):
            # add \n if more than one line and not last line
            if len(content) > 1 and i != len(content) - 1:
                content_string += f"{line.text}\n"
            else:
                content_string += line.text

    return content_string
