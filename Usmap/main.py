import io
from typing import List
import brotli
from Usmap.Oodle import Decompress

from Usmap.BinaryReader import BinaryStream
from Usmap.Objects.FPropertyTag import FPropertyTag
from Usmap.Objects.FName import FName


class Usmap:
    MAGIC = 0x30C4
    NameMap: List[str]
    Enums: dict
    Mappings: dict

    def __init__(self, IO) -> None:
        self.reader = BinaryStream(IO)
        self.Mappings = {}
        self.Enums = {}

    def read(self):
        reader = self.reader

        magic = reader.readInt16()
        if magic != self.MAGIC:
            raise Exception("invalid magic")

        version = reader.readByteToInt()

        if version != 0:  # Initial
            raise Exception(".usmap file has invalid version $version")

        method = reader.readByteToInt()
        compressSize = reader.readInt32()
        decompressSize = reader.readInt32()

        # 0 -> "None"
        # 1 -> "Oodle"
        # 2 -> "Brotli"
        decompressedData: bytes
        if method == 0:
            decompressedData = reader.readBytes(compressSize)
        elif method == 1:
            decompressedData = Decompress(reader.readBytes(compressSize),decompressSize)
        elif method == 2:
            decompressedData = brotli.decompress(reader.readBytes(compressSize))
        else:
            raise Exception("Unknown compression method")

        if len(decompressedData) != decompressSize:
            raise ValueError(f"Failed to decompress data, Expected length {decompressSize} got {len(decompressedData)}")

        self.reader = BinaryStream(io.BytesIO(decompressedData))
        self.ParseData()
        return self

    def ParseData(self):
        reader = self.reader

        self.NameMap = reader.readTArray(reader.readFString)

        # Enums
        size = reader.readUInt32()
        for _ in range(size):
            enumName = reader.readFName(self.NameMap)
            Number = reader.readByteToInt()
            Values = []
            for _ in range(Number):
                Name = reader.readFName(self.NameMap).string  # FName
                Values.append(Name)

            self.Enums[enumName.string] = []
            self.Enums[enumName.string] = Values

        # Schemas
        size = reader.readUInt32()
        for _ in range(size):
            struct: Struct = Struct()
            struct.Name = reader.readFName(self.NameMap).string
            struct.SuperIndex = reader.readUInt32()
            struct.PropertyCount = reader.readUInt16()

            serializablePropertyCount = reader.readUInt16()
            props = {}
            for _ in range(serializablePropertyCount):
                prop: StructProps = StructProps()
                prop.SchemaIndex = reader.readUInt16()
                prop.ArraySize = reader.readByteToInt()
                prop.Name = reader.readFName(self.NameMap).string
                prop.data = FPropertyTag(reader, self)
                props[prop.SchemaIndex] = prop

            struct.props = props
            self.Mappings[struct.Name] = struct


class StructProps:
    SchemaIndex: int
    ArraySize: int
    Name: FName
    data: FPropertyTag

    def __init__(self):
        pass


class Struct:
    Name: FName
    SuperIndex: int
    PropertyCount: int
    props: StructProps

    def __init__(self):
        pass
