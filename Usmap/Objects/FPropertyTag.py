from Usmap.Objects.FName import FName
from Usmap.BinaryReader import BinaryStream
from enum import IntEnum, auto


class FPropertyTag:
    StructName: FName
    ValueType = None  # self
    EnumName: FName
    InnerType = None  # self

    def __init__(self, reader: BinaryStream, usmap) -> None:
        NameMap = usmap.NameMap

        Type = reader.readByteToInt()
        try:
            self.Type = EUsmapPropertyType(Type).name
        except:
            print(f"USMAP Reader: Invalid PropertyType Value {Type}")
            self.Type = Type

        if Type == EUsmapPropertyType.StructProperty.value:
            self.StructName = reader.readFName(NameMap)

        elif Type == EUsmapPropertyType.EnumProperty.value:
            self.InnerType = FPropertyTag(reader, usmap)
            self.EnumName = reader.readFName(NameMap)

        elif Type == EUsmapPropertyType.ArrayProperty.value:
            self.InnerType = FPropertyTag(reader, usmap)

        elif Type == EUsmapPropertyType.SetProperty.value:  # same as Array
            self.InnerType = FPropertyTag(reader, usmap)

        elif Type == EUsmapPropertyType.MapProperty.value:
            self.InnerType = FPropertyTag(reader, usmap)
            self.ValueType = FPropertyTag(reader, usmap)


class EUsmapPropertyType(IntEnum):
    ByteProperty = 0
    BoolProperty = auto()
    IntProperty = auto()
    FloatProperty = auto()
    ObjectProperty = auto()
    NameProperty = auto()
    DelegateProperty = auto()
    DoubleProperty = auto()
    ArrayProperty = auto()
    StructProperty = auto()
    StrProperty = auto()
    TextProperty = auto()
    InterfaceProperty = auto()
    MulticastDelegateProperty = auto()
    WeakObjectProperty = auto()
    LazyObjectProperty = auto()
    AssetObjectProperty = auto()
    SoftObjectProperty = auto()
    UInt64Property = auto()
    UInt32Property = auto()
    UInt16Property = auto()
    Int64Property = auto()
    Int16Property = auto()
    Int8Property = auto()
    MapProperty = auto()
    SetProperty = auto()
    EnumProperty = auto()
    FieldPathProperty = auto()
