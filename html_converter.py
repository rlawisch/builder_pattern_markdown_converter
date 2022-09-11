import re
from text_converter import TextConverter

class HTMLConverter(TextConverter):
    def __init__(self, text: str) -> None:
        self.__text = text

    @property
    def text(self) -> str:
        return self.__text

    def convert(self) -> str:
        self.convert_unordered_list()
        self.convert_bold()
        self.convert_italics()
        self.convert_headers()
        return self.__text

    def convert_headers(self) -> str:
        self.__text = re.sub(r'<\|start:h([1-6])\|>', r'<h\1>', self.__text)
        self.__text = re.sub(r'<\|end:h([1-6])\|>', r'</h\1>', self.__text)

    def convert_bold(self) -> str:
        self.__text = self.__text.replace('<|start:bold|>', '<strong>')
        self.__text = self.__text.replace('<|end:bold|>', '</strong>')

    def convert_italics(self) -> str:
        self.__text = self.__text.replace('<|start:italics|>', '<em>')
        self.__text = self.__text.replace('<|end:italics|>', '</em>')

    def convert_unordered_list(self) -> str:
        self.__text = self.__text.replace('<|start:unordered_list|>', '<ul>')
        self.__text = self.__text.replace('<|end:unordered_list|>', '</ul>')
        self.__text = self.__text.replace('<|start:unordered_list_item|>', '\t<li>')
        self.__text = self.__text.replace('<|end:unordered_list_item|>', '</li>')
