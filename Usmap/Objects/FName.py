from Usmap.Objects.FNameEntrySerialized import FNameEntrySerialized


class FName:
    Index: int
    Number: int
    String: FNameEntrySerialized
    string: str
    isNone: bool

    def __init__(self, name: FNameEntrySerialized, index: int, number: int) -> None:
        self.string = name
        self.Index = index
        self.Number = number

    @property
    def isNone(self):
        return self.string is None or self.string == "None"

    def GetValue(self):
        return self.string
