
from abc import abstractmethod

class ICallMyAccessor:
    @abstractmethod
    def add(self, v: int) -> None:
        pass

    @abstractmethod
    def get(self) -> list[int]:
        pass

    @abstractmethod
    def print(self) -> None:
        pass
