from abc import ABCMeta, abstractmethod

class TextConverter(metaclass=ABCMeta):
    @property
    @abstractmethod
    def text(self):
        pass

    @abstractmethod
    def convert(self) -> str:
        pass
