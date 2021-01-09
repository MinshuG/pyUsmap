class FNameEntrySerialized:
    Name = None

    def __init__(self, reader) -> None:
        self.Name = reader.readFString()
        reader.seek(4)  # Dummy
