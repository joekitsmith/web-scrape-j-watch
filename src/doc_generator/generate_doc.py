from pathlib import Path
import json
import re

from docx import Document
from docx.shared import Cm, Pt
from docx.shared import RGBColor
from docx.oxml.shared import qn
from docx.oxml.xmlchemy import OxmlElement


def add_line_breaks(content_list):
    content_string = ""
    for line in content_list:
        content_string += f"{line}\n\n"

    return content_string


class DocumentGenerator:
    def create_document(self, data):
        self.document = Document()
        margin = 2.4
        sections = self.document.sections
        for section in sections:
            section.top_margin = Cm(margin)
            section.bottom_margin = Cm(margin)
            section.left_margin = Cm(margin)
            section.right_margin = Cm(margin)

        self.title = data["Title"]
        self.contributors = data["Contributors"]
        self.summary = data["Summary"]
        self.main_content = add_line_breaks(data["MainContent"])
        self.comment_header = data["CommentHeader"]
        self.comment_content = data["CommentContent"]
        # self.citations_header = data["CitationsHeader"]
        # self.citations_content = data["CitationsContent"]

        print(self.title)

        self.create_heading()
        self.create_contributors()
        self.create_summary()
        self.create_main_content()

        if self.comment_header is not None:
            self.create_comment()

        # self.create_citations()
        save_name = re.sub(r"\W+", "", self.title.lower().replace(" ", "_"))
        self.document.save(f"{save_name}.docx")

    def get_example_paper(self) -> None:
        root_dir = Path(__file__).parent.resolve()
        with open(f"{root_dir}/example_paper.json") as f:
            example = json.load(f)

        return example

    def create_heading(self):
        run = self.document.add_paragraph().add_run(self.title)
        font = run.font
        font.name = "Arial"
        font.size = Pt(24)
        font.bold = True
        font.color.rgb = RGBColor(99, 62, 106)

    def create_contributors(self):
        run = self.document.add_paragraph().add_run(self.contributors)
        font = run.font
        font.name = "Times New Roman"
        font.size = Pt(9)
        font.italic = True

    def create_summary(self):
        run = self.document.add_paragraph().add_run(self.summary)
        font = run.font
        font.name = "Arial"
        font.size = Pt(9)
        font.italic = True
        font.color.rgb = RGBColor(0, 0, 0)

    def create_main_content(self):
        paragraph = self.document.add_paragraph()
        paragraph.paragraph_format.space_after = Pt(0)
        run = paragraph.add_run(self.main_content)
        font = run.font
        font.name = "Arial"
        font.size = Pt(9)
        font.color.rgb = RGBColor(0, 0, 0)

    def create_comment(self):
        table = self.document.add_table(rows=2, cols=1)
        header_cell = table.rows[0].cells[0]
        body_cell = table.rows[1].cells[0]

        header_cell.text = self.comment_header
        body_cell.text = self.comment_content

        if self.comment_header is not None:
            for i in range(2):
                self._set_cell_background(table.rows[i].cells[0], "E3E9F0")

            for i, row in enumerate(table.rows):
                for cell in row.cells:
                    paragraphs = cell.paragraphs
                    for paragraph in paragraphs:
                        for run in paragraph.runs:
                            font = run.font
                            if i == 0:
                                font.size = Pt(14)
                                font.bold = True
                            if i == 1:
                                font.name = "Arial"
                                font.size = Pt(9)

    def create_citations(self):
        paragraph = self.document.add_paragraph()
        paragraph.paragraph_format.space_before = Pt(15)
        run = paragraph.add_run(self.citations_header)
        font = run.font
        font.size = Pt(12)
        font.bold = True

        run = self.document.add_paragraph().add_run(self.citations_content)
        font = run.font
        font.name = "Arial"
        font.size = Pt(9)

    def _set_cell_background(self, cell, fill, color=None, val=None):
        """
        @fill: Specifies the color to be used for the background
        @color: Specifies the color to be used for any foreground
        pattern specified with the val attribute
        @val: Specifies the pattern to be used to lay the pattern
        color over the background color.
        """

        cell_properties = cell._element.tcPr
        try:
            cell_shading = cell_properties.xpath("w:shd")[
                0
            ]  # in case there's already shading
        except IndexError:
            cell_shading = OxmlElement("w:shd")  # add new w:shd element to it
        if fill:
            cell_shading.set(
                qn("w:fill"), fill
            )  # set fill property, respecting namespace
        if color:
            pass  # TODO
        if val:
            pass  # TODO
        cell_properties.append(
            cell_shading
        )  # finally extend cell props with shading element
