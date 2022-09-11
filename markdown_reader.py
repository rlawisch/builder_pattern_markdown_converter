import re
from text_converter import TextConverter
from html_converter import HTMLConverter

class MarkdownReader:
    def __init__(self, text) -> None:
        self.__converter: TextConverter = None
        self.__parsed_text = self._parse_text(text)

    def to_html(self):
        self.__converter = HTMLConverter(self.__parsed_text)
        return self

    def convert(self) -> str:
        return self.__converter.convert()

    def _parse_text(self, text):
        parsed_text = self._parse_unordered_list(text)
        parsed_text = self._parse_bold(parsed_text)
        parsed_text = self._parse_italics(parsed_text)
        parsed_text = self._parse_h6(parsed_text)
        parsed_text = self._parse_h5(parsed_text)
        parsed_text = self._parse_h4(parsed_text)
        parsed_text = self._parse_h3(parsed_text)
        parsed_text = self._parse_h2(parsed_text)
        parsed_text = self._parse_h1(parsed_text)
        return parsed_text

    def _parse_h1(self, text) -> str:
        return re.sub(r"((?<!\\)#){1} ([^\n$]+)", r"<|start:h1|>\2<|end:h1|>", text)

    def _parse_h2(self, text) -> str:
        return re.sub(r"((?<!\\)#){2} ([^\n$]+)", r"<|start:h2|>\2<|end:h2|>", text)

    def _parse_h3(self, text) -> str:
        return re.sub(r"((?<!\\)#){3} ([^\n$]+)", r"<|start:h3|>\2<|end:h3|>", text)

    def _parse_h4(self, text) -> str:
        return re.sub(r"((?<!\\)#){4} ([^\n$]+)", r"<|start:h4|>\2<|end:h4|>", text)

    def _parse_h5(self, text) -> str:
        return re.sub(r"((?<!\\)#){5} ([^\n$]+)", r"<|start:h5|>\2<|end:h5|>", text)

    def _parse_h6(self, text) -> str:
        return re.sub(r"((?<!\\)#){6} ([^\n$]+)", r"<|start:h6|>\2<|end:h6|>", text)

    def _parse_italics(self, text) -> str:
        return re.sub(r"((?<!\\)\*){1}([^\n(\*)$]+)\1{1}", r"<|start:italics|>\2<|end:italics|>", text)

    def _parse_bold(self, text) -> str:
        return re.sub(r"((?<!\\)\*){2}([^\n(\*\*)$]+)\1{2}", r"<|start:bold|>\2<|end:bold|>", text)

    def _parse_unordered_list(self, text) -> str:
        lines = text.splitlines()
        is_in_list = False
        list_item_regex = re.compile(r"^\s*-\s([^\n]+)")

        for i, line in enumerate(lines):
            if list_item_regex.match(line):
                lines[i] = re.sub(list_item_regex, r"<|start:unordered_list_item|>\1<|end:unordered_list_item|>", line)

                if not is_in_list:
                    lines[i] = f"<|start:unordered_list|>\n{lines[i]}"
                    is_in_list = True

            elif is_in_list:
                lines[i] = f"<|end:unordered_list|>\n{line}"
                is_in_list = False

        parsed_text = '\n'.join(lines)

        if is_in_list:
            parsed_text = f"{parsed_text}\n<|end:unordered_list|>"

        return parsed_text
