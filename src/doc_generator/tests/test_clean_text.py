from pathlib import Path
import sys

root_dir = (Path(__file__).parent / "../").resolve()
sys.path.append(str(root_dir))

from clean_text import clean_text, remove_open_in_new_tab, add_line_breaks
from web_scraper.data_classes import Line


class TestCleanText:
    def test_clean_text_twoLines(self):
        # assemble
        line_list = [Line("line_1"), Line("line_2")]
        # act
        string = clean_text(line_list)
        # assert
        assert string == "line_1\nline_2"


class TestRemoveOpenInNewTab:
    def test_remove_open_in_new_tab_lineWithNoMarker_noOpenInNewTab(self):
        # assemble
        line_list = [Line("line_1")]
        # act
        output_line_list = remove_open_in_new_tab(line_list)
        # assert
        assert output_line_list == [Line("line_1")]

    def test_remove_open_in_new_tab_lineWithMarker_noOpenInNewTab(self):
        # assemble
        line_list = [Line("line_1", True)]
        # act
        output_line_list = remove_open_in_new_tab(line_list)
        # assert
        assert output_line_list == [Line("line_1", True)]

    def test_remove_open_in_new_tab_lineWithNoMarker_OpenInNewTabPresent(self):
        # assemble
        line_list = [Line("line_1\n. opens in new tab\n")]
        # act
        output_line_list = remove_open_in_new_tab(line_list)
        # assert
        assert output_line_list == [Line("line_1.")]

    def test_remove_open_in_new_tab_lineListEmpty(self):
        # assemble
        line_list = []
        # act
        output_line_list = remove_open_in_new_tab(line_list)
        # assert
        assert output_line_list == []

    def test_remove_open_in_new_tab_lineListNotAList(self):
        # assemble
        line_list = ""
        # act
        output_line_list = remove_open_in_new_tab(line_list)
        # assert
        assert output_line_list == []


class TestAddLineBreaks:
    def test_add_line_breaks_oneLine(self):
        # assemble
        line_list = [Line("line_1")]
        # act
        string = add_line_breaks(line_list)
        # assert
        assert string == "line_1"

    def test_add_line_breaks_twoLines(self):
        # assemble
        line_list = [Line("line_1"), Line("line_2")]
        # act
        string = add_line_breaks(line_list)
        # assert
        assert string == "line_1\nline_2"

    def test_add_line_breaks_emptyList(self):
        # assemble
        line_list = []
        # act
        string = add_line_breaks(line_list)
        # assert
        assert string == ""

    def test_add_line_breaks_lineListNotList(self):
        # assemble
        line_list = ""
        # act
        string = add_line_breaks(line_list)
        # assert
        assert string == ""
