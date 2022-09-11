from markdown_reader import MarkdownReader
import unittest

class TestMarkdownReader(unittest.TestCase):
    def test_h1_one_line(self) -> None:
        parser = MarkdownReader("# First header").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "<h1>First header</h1>")

    def test_h1_multi_line(self) -> None:
        parser = MarkdownReader("This is a\n# Header\nin multiline text").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "This is a\n<h1>Header</h1>\nin multiline text")

    def test_h2_one_line(self) -> None:
        parser = MarkdownReader("## Second header").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "<h2>Second header</h2>")

    def test_h2_multi_line(self) -> None:
        parser = MarkdownReader("This is a\n## Second header\nin multiline text").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "This is a\n<h2>Second header</h2>\nin multiline text")

    def test_h3_one_line(self) -> None:
        parser = MarkdownReader("### Third header").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "<h3>Third header</h3>")

    def test_h3_multi_line(self) -> None:
        parser = MarkdownReader("This is a\n### Third header\nin multiline text").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "This is a\n<h3>Third header</h3>\nin multiline text")

    def test_h4_one_line(self) -> None:
        parser = MarkdownReader("#### Fourth header").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "<h4>Fourth header</h4>")

    def test_h4_multi_line(self) -> None:
        parser = MarkdownReader("This is a\n#### Fourth header\nin multiline text").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "This is a\n<h4>Fourth header</h4>\nin multiline text")

    def test_h5_one_line(self) -> None:
        parser = MarkdownReader("##### Fifth header").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "<h5>Fifth header</h5>")

    def test_h5_multi_line(self) -> None:
        parser = MarkdownReader("This is a\n##### Fifth header\nin multiline text").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "This is a\n<h5>Fifth header</h5>\nin multiline text")

    def test_h6_one_line(self) -> None:
        parser = MarkdownReader("###### Sixth header").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "<h6>Sixth header</h6>")

    def test_h6_multi_line(self) -> None:
        parser = MarkdownReader("This is a\n###### Sixth header\nin multiline text").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "This is a\n<h6>Sixth header</h6>\nin multiline text")

    def test_italics(self) -> None:
        parser = MarkdownReader("Test some *italics* text").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "Test some <em>italics</em> text")

    def test_multiple_italics(self) -> None:
        parser = MarkdownReader("Test *more* than one *italics* text").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "Test <em>more</em> than one <em>italics</em> text")

    def test_bold(self) -> None:
        parser = MarkdownReader("Test some **booold** text").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "Test some <strong>booold</strong> text")

    def test_multiple_bold(self) -> None:
        parser = MarkdownReader("Test **more** than one **bold** text").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "Test <strong>more</strong> than one <strong>bold</strong> text")

    def test_bold_italics(self) -> None:
        parser = MarkdownReader("Test some ***really highlighted*** text").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "Test some <em><strong>really highlighted</strong></em> text")

    def test_multiple_bold_italics(self) -> None:
        parser = MarkdownReader("Test ***more*** than one ***really highlighted*** text").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "Test <em><strong>more</strong></em> than one <em><strong>really highlighted</strong></em> text")

    def test_unordered_list(self) -> None:
        parser = MarkdownReader("This is a list:\n- Item 1\n- Item 2").to_html()
        parsed_html = parser.convert()
        self.assertEqual(parsed_html, "This is a list:\n<ul>\n\t<li>Item 1</li>\n\t<li>Item 2</li>\n</ul>")


if __name__ == '__main__':
    unittest.main()
