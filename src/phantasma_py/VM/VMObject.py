from ast import Dict
import base64
from ctypes import Union
from datetime import datetime
from email.headerregistry import Address
from ..Types.Timestamp import Timestamp
from .VMType import VMType
from typing import Dict, Union

#import big_int  # Assuming big_int is a Python equivalent of big-integer library


class VMObject:
    TimeFormat = "%m/%d/%Y %H:%M:%S"

    def __init__(self):
        self.Type = VMType.NONE
        self.Data = None
        self._local_size = 0

    @property
    def IsEmpty(self):
        return self.Data is None

    def GetChildren(self) -> Union[Dict['VMObject', 'VMObject'], None]:
        return self.Data if self.Type == VMType.Struct else None

    @property
    def Size(self):
        if self.Type == VMType.Object:
            children = self.GetChildren()
            total = sum(entry.Size for entry in children.values())
        else:
            total = self._localSize

        return total

    def AsType(self, type):
        if type == VMType.Bool:
            return self.AsBool()
        elif type == VMType.String:
            return self.AsString()
        elif type == VMType.Bytes:
            return self.AsByteArray()
        elif type == VMType.Number:
            return self.AsNumber()
        elif type == VMType.Timestamp:
            return self.AsTimestamp()
        else:
            raise ValueError("Unsupported VM cast")

    def AsEnum(self, enum_type):
        if not issubclass(enum_type, Enum):
            raise ValueError("enum_type must be an enumerated type")

        if self.Type != VMType.Enum:
            num = self.AsNumber()
            self.Data = int(num)

        return enum_type(self.Data)

    def AsNumber(self):
        if (self.Type in [VMType.Object, VMType.Timestamp]) and isinstance(self.Data, Timestamp):
            return self.Data.Value

        if self.Type == VMType.NONE:
            return 0

        if self.Type == VMType.String:
            if str(self.Data).isnumeric():
                return int(self.Data)
            else:
                raise Exception(f"Cannot convert String '{self.Data}' to BigInteger.")

        if self.Type == VMType.Bytes:
            bytes_data = bytes(self.Data)
            return int.from_bytes(bytes_data, byteorder='big', signed=False)

        if self.Type == VMType.Enum:
            return int(self.Data)

        if self.Type == VMType.Bool:
            return int(self.Data)

        if self.Type == VMType.Object and isinstance(self.Data, Hash):
            hash_obj = self.Data
            return hash_obj.AsNumber()

        if self.Type != VMType.Number:
            raise Exception(f"Invalid cast: expected number, got {self.Type}")

        return self.Data

    def AsTimestamp(self):
        if self.Type != VMType.Timestamp:
            raise Exception(f"Invalid cast: expected timestamp, got {self.Type}")

        return self.Data
    
    def AsString(self):
        if self.Type == VMType.String:
            return str(self.Data)

        if self.Type == VMType.Number:
            return str(int(self.Data))

        if self.Type == VMType.Bytes:
            return self.Data.decode('utf-8')

        if self.Type == VMType.Enum:
            return str(self.Data)

        if self.Type == VMType.Object:
            if isinstance(self.Data, Address):
                return self.Data.Text
            elif isinstance(self.Data, Hash):
                return str(self.Data)
            else:
                return "Interop:" + type(self.Data).__name__

        if self.Type == VMType.Struct:
            array_type = self.GetArrayType()
            if array_type == VMType.Number:
                children = self.GetChildren()
                result = ""
                for i in range(len(children)):
                    key = VMObject.FromObject(i)
                    val = children[key]
                    ch = chr(int(val.AsNumber()))
                    result += ch
                return result
            else:
                with np.nditer(self.Data, flags=['multi_index'], op_flags=['readonly']) as it:
                    result = bytearray()
                    while not it.finished:
                        index = it.multi_index
                        element = self.Data[index]
                        if isinstance(element, bytes):
                            result.extend(element)
                        else:
                            result.append(element)
                        it.iternext()
                    return base64.b64encode(result).decode('utf-8')

        if self.Type == VMType.Bool:
            return "true" if self.Data else "false"

        if self.Type == VMType.Timestamp:
            date = self.Data
            return date.Value.strftime("%m/%d/%Y %H:%M:%S")

        raise Exception(f"Invalid cast: expected string, got {self.Type}")

    def AsArray(self, type):
        if self.Type != VMType.Struct:
            raise Exception(f"Invalid cast: expected struct, got {self.Type}")

        if self.Data is None:
            return []

        values = self.Data

        if not isinstance(values, dict):
            raise Exception("Invalid struct data")

        result = []

        for i in range(len(values)):
            key = VMObject.FromObject(i)
            val = VMObject.FromObject(values.get(key))
            result.append((val, type))

        return result
    
    def GetArrayType(self):
        if self.Type != VMType.Struct:
            return VMType.NONE

        children = self.GetChildren()

        result = VMType.NONE

        for i in range(len(children)):
            key = VMObject.FromObject(i)

            if key not in children:
                return VMType.NONE

            val = children[key]

            if result == VMType.NONE:
                result = val.Type
            elif val.Type != result:
                return VMType.NONE

        return result

    def AsByteArray(self):
        if self.Type == VMType.Bytes:
            return bytes(self.Data)

        if self.Type == VMType.Bool:
            return bytes([int(self.Data)])

        if self.Type == VMType.String:
            str_data = self.AsString()
            return str_data.encode('utf-8')

        if self.Type == VMType.Number:
            num_data = self.AsNumber()
            return num_data.to_bytes((num_data.bit_length() + 7) // 8, byteorder='big', signed=True)

        if self.Type == VMType.Enum:
            num_data = int(self.AsNumber())
            return num_data.to_bytes(4, byteorder='big', signed=False)

        if self.Type == VMType.Timestamp:
            time_data = self.AsTimestamp()
            return time_data.Value.to_bytes(8, byteorder='big', signed=False)

        if self.Type == VMType.Struct:
            return self.Serialize()

        if self.Type == VMType.Object:
            serializable = self.Data
            if isinstance(serializable, ISerializable):
                serial_data = serializable.Serialize()[1:]
                return bytearray(serial_data)

            raise Exception("Complex object type can't be converted to bytes")

        raise Exception(f"Invalid cast: expected bytes, got {self.Type}")
    
    def AsAddress(self):
        if self.Type == VMType.String:
            temp = str(self.Data)
            if Address.IsValidAddress(temp):
                return Address.FromText(temp)

        if self.Type == VMType.Bytes:
            temp = bytes(self.Data)

            if len(temp) == Address.LengthInBytes + 1:
                temp = temp[1:]  # Remove the first byte

            if len(temp) == Address.LengthInBytes:
                return Address.FromBytes(temp)

            raise Exception(f"Invalid address size, expected {Address.LengthInBytes} got {len(temp)}")

        if self.Type == VMType.Object and isinstance(self.Data, Address):
            return self.Data

        raise Exception(f"Invalid cast: expected address, got {self.Type}")

    def AsBool(self):
        if self.Type == VMType.Bytes:
            bytes_data = bytes(self.Data)
            if len(bytes_data) == 1:
                return bytes_data[0] != 0

        if self.Type == VMType.Bool:
            return bool(self.Data)

        if self.Type == VMType.Number:
            val = self.AsNumber()
            return val != 0

        raise Exception(f"Invalid cast: expected bool, got {self.Type}")

    def AsStruct(self, struct_type):
        if self.Type == VMType.Object:
            if self.Data is not None and isinstance(self.Data, struct_type):
                return self.Data
            else:
                raise Exception(f"Invalid cast: expected VMObject of type {struct_type.__name__}")

        if self.Type != VMType.Struct:
            raise Exception(f"Invalid cast: expected struct, got {self.Type}")

        if self.Data is None:
            return None

        values = self.Data

        if not isinstance(values, dict):
            raise Exception("Invalid struct data")

        result = struct_type()

        # WARNING: This code is experimental and might not work in every situation.
        for entry in values.items():
            key = entry[0]
            field_name = key.AsString()

            if not field_name:
                raise Exception("Key with null or non-string name found in struct")

            if not hasattr(struct_type, field_name):
                raise Exception("Unknown field: " + field_name)

            field = getattr(struct_type, field_name)
            field_type = field.__annotations__['value']

            field_value = entry[1].ToStruct(field_type) if entry[1].Type == VMType.Struct else entry[1].ToObject()
            field_value = field_value if field_value is not None else ''

            try:
                setattr(result, field_name, field_value)
            except Exception as e:
                raise Exception(f"Could not set field value: {field_name}, {e}")

        return result
    

    @staticmethod
    def ConvertObjectInternal(field_value, field_type):
        if field_type == VMObject:
            # Edge case: happens when calling ToArray<VMObject>()
            return VMObject.FromObject(field_value)
        elif inspect.isclass(field_type) or inspect.isclass(field_value):
            # Check if it's a struct or class and the value is a byte array
            if isinstance(field_value, bytes):
                field_value = Serialization.Unserialize(field_value, field_type)
        elif inspect.isclass(field_type) and issubclass(field_type, enum.Enum):
            # If it's an enum, parse it based on its type
            field_value = field_type(field_value)

        return field_value

    def AsInterop(self, interop_type):
        if interop_type == Hash and self.Type != VMType.Object:
            bytes_data = self.AsByteArray()

            if len(bytes_data) == 33 and bytes_data[0] == 32:
                bytes_data = bytes_data[1:]

            if len(bytes_data) == 32:
                return Hash(bytes_data)

        if self.Type != VMType.Object:
            raise Exception(f"Invalid cast: expected object, got {self.Type}")

        if self.Data is None:
            return None

        if not isinstance(self.Data, interop_type):
            raise Exception("Invalid interop type")

        return self.Data
    
    def SetValue(self, val, vm_type):
        self.Type = vm_type
        self._localSize = len(val) if val is not None else 0

        if vm_type == VMType.Bytes:
            self.Data = val
        elif vm_type == VMType.Number:
            self.Data = BigInteger(0) if val is None or len(val) == 0 else BigInteger(val)
        elif vm_type == VMType.String:
            self.Data = val.decode('utf-8') if val is not None else ""
        elif vm_type == VMType.Enum:
            self.Data = int.from_bytes(val, byteorder='big', signed=False)
        elif vm_type == VMType.Timestamp:
            temp = 0 if val is None else int.from_bytes(val, byteorder='big', signed=False)
            self.Data = Timestamp(temp)
        elif vm_type == VMType.Bool:
            self.Data = bool.from_bytes(val, byteorder='big', signed=False)
        else:
            if isinstance(val, bytes):
                bytes_val = val
                length = len(bytes_val) if bytes_val is not None else 0

                if length == Address.LengthInBytes:
                    self.Data = Address.FromBytes(bytes_val)
                elif length == Hash.Length:
                    self.Data = Hash.FromBytes(bytes_val)
                else:
                    try:
                        self.UnserializeData(bytes_val)
                    except Exception as e:
                        raise Exception("Cannot decode interop object from bytes with length: " + str(length))
            else:
                raise Exception("Cannot set value for VMType: " + vm_type)

        return self

    ''' elif isinstance(val, Hash):
                self.Type = VMType.Object
                self.Data = val
                self._localSize = 4'''
    def SetValue(self, val):
        if isinstance(val, int):
            self.Type = VMType.Number
            self.Data = val
            self._localSize = len(val.to_bytes((val.bit_length() + 7) // 8, byteorder='big', signed=True))
        elif isinstance(val, dict):
            for key in val.keys():
                self.ValidateStructKey(key)
            self.Type = VMType.Struct
            self.Data = val
            self._localSize = 4  # TODO: Update this value
        elif isinstance(val, Address):
            self.Type = VMType.Object
            self.Data = val
            self._localSize = 4
        elif isinstance(val, Timestamp):
            self.Type = VMType.Timestamp
            self.Data = val
            self._localSize = 4
        elif isinstance(val, str):
            self.Type = VMType.String
            self.Data = val
            self._localSize = len(val)
        elif isinstance(val, bool):
            self.Type = VMType.Bool
            self.Data = val
            self._localSize = 1
        elif isinstance(val, bytes):
            self.Type = VMType.Bytes
            self.Data = val
            self._localSize = len(val)
        elif isinstance(val, enum.Enum):
            self.Type = VMType.Enum
            self.Data = val
            self._localSize = 4
        else:
            val_type = type(val)
            if val is not None and val_type == Timestamp:
                return self.SetValue(val)
            if not inspect.isclass(val_type) or not val_type.__annotations__ or 'value' not in val_type.__annotations__:
                raise Exception(f"Invalid cast: expected struct or class, got {val_type.__name__}")
            self.Type = VMType.Object
            self.Data = val
            self._localSize = 4
        return self

    @staticmethod
    def ValidateStructKey(key):
        if key.Type in [VMType.NONE, VMType.Struct, VMType.Object]:
            raise Exception(f"Cannot use value of type {key.Type} as key for struct field")

    def SetDefaultValue(self, vm_type):
        self.Type = vm_type
        self._localSize = 1  # TODO: Fixme

        if vm_type == VMType.Bytes:
            self.Data = bytearray()
        elif vm_type == VMType.Number:
            self.Data = int(0)
        elif vm_type == VMType.String:
            self.Data = ""
        elif vm_type == VMType.Enum:
            self.Data = 0
        elif vm_type == VMType.Timestamp:
            self.Data = Timestamp(0)
        elif vm_type == VMType.Bool:
            self.Data = False
        elif vm_type == VMType.Object:
            self.Data = None
        else:
            raise Exception("Cannot initialize default value for VMType: " + vm_type)

        return self
    
    def SetKey(self, key, obj):
        self.ValidateStructKey(key)
        children = {}

        # NOTE: In Python, we don't need to create a new VMObject instance for the key
        if self.Type == VMType.Struct:
            children = self.GetChildren()
        elif self.Type == VMType.NONE:
            self.Type = VMType.Struct
            children = {}
            self.Data = children
            self._localSize = 0
        else:
            raise Exception(f"Invalid cast from {self.Type} to struct")

        children[key] = obj

    def GetField(self, key):
        key_obj = VMObject.FromObject(key)
        return self.GetField(key_obj)

    def GetField(self, key):
        if self.Type != VMType.Struct:
            raise Exception(f"Invalid cast: expected struct, got {self.Type}")

        children = self.GetChildren()

        return children.get(key, VMObject())
    
    def GetHashCode(self):
        if self.Type == VMType.Struct:
            hash_value = 2166136261
            children = self.GetChildren()
            for child in children:
                hash_value = (hash_value * 16777619 + child.GetHashCode()) & 0xFFFFFFFF  # Ensure the hash value is within 32-bit bounds
            return hash_value
        else:
            return hash(self.Data) if self.Data is not None else 0

    def Equals(self, other):
        if other is None:
            return False

        if not isinstance(other, VMObject):
            return False

        if self.Type != other.Type:
            return False

        if self.Type == VMType.Struct:
            children = self.GetChildren()
            other_children = other.GetChildren()

            for key, value in children.items():
                if key not in other_children:
                    return False

                if value != other_children[key]:
                    return False

            for key, value in other_children.items():
                if key not in children:
                    return False

            return True
        else:
            return self.Data == other.Data

    def Copy(self, other):
        if other is None or other.Type == VMType.NONE:
            self.Type = VMType.NONE
            self.Data = None
            return

        self.Type = other.Type

        if other.Type == VMType.Struct:
            children = {}
            other_children = other.GetChildren()
            for key in other_children.keys():
                temp = VMObject()
                temp.Copy(other_children[key])
                children[key] = temp

            self.Data = children
        else:
            self.Data = other.Data

    def ToString(self):
        if self.Type == VMType.NONE:
            return "Null"
        elif self.Type == VMType.Struct:
            return "[Struct]"
        elif self.Type == VMType.Bytes:
            return f"[Bytes] => {Base16.Encode(self.Data)}"
        elif self.Type == VMType.Number:
            return f"[Number] => {self.Data}"
        elif self.Type == VMType.Timestamp:
            return f"[Time] => {self.Data.strftime(TimeFormat)}"
        elif self.Type == VMType.String:
            return f"[String] => {self.Data}"
        elif self.Type == VMType.Bool:
            return f"[Bool] => {self.Data}"
        elif self.Type == VMType.Enum:
            return f"[Enum] => {self.Data}"
        elif self.Type == VMType.Object:
            return f"[Object] => {self.Data.__class__.__name__ if self.Data is not None else 'null'}"
        else:
            return "Unknown"

    @staticmethod
    def CastTo(src_obj, type):
        if src_obj.Type == type:
            result = VMObject()
            result.Copy(src_obj)
            return result

        if type == VMType.NONE:
            return VMObject()

        result = VMObject()

        if type == VMType.String:
            result.SetValue(src_obj.AsString())
        elif type == VMType.Timestamp:
            result.SetValue(src_obj.AsTimestamp())
        elif type == VMType.Bool:
            result.SetValue(src_obj.AsBool())
        elif type == VMType.Bytes:
            result.SetValue(src_obj.AsByteArray())
        elif type == VMType.Number:
            result.SetValue(src_obj.AsNumber())
        elif type == VMType.Struct:
            if src_obj.Type == VMType.String:
                str_value = src_obj.AsString()
                chars = [VMObject.FromObject(BigInteger(ord(c))) for c in str_value]
                return VMObject.FromArray(chars)
            elif src_obj.Type == VMType.Object:
                # You'll need to implement the equivalent of CastViaReflection here.
                # This code depends on your specific class and object structure.
                # Please provide additional information about CastViaReflection to complete this part.
                pass
            else:
                raise Exception(f"Invalid cast: {src_obj.Type} to {type}")
        else:
            raise Exception(f"Invalid cast: {src_obj.Type} to {type}")

        return result
    
    @staticmethod
    def GetVMType(type):
        if type == VMType.Enum:
            return VMType.Enum
        elif type == bool:
            return VMType.Bool
        elif type == str:
            return VMType.String
        elif type == bytes:
            return VMType.Bytes
        elif type == int or type == BigInteger:
            return VMType.Number
        elif type == Timestamp or type == uint:
            return VMType.Timestamp
        elif type.__class__.__name__ == 'Enum':
            return VMType.Enum
        elif type.__class__.__name__ == 'list':
            return VMType.Struct
        elif hasattr(type, '__class__') and (type.__class__.__name__ == 'classobj' or type.__class__.__name__ == 'type'):
            return VMType.Object
        else:
            return VMType.NONE

    @staticmethod
    def IsVMType(type):
        result = VMObject.GetVMType(type)
        return result != VMType.NONE

    @staticmethod
    def FromArray(array):
        result = VMObject()
        for i in range(len(array)):
            key = VMObject.FromObject(i)

            temp = array[i]
            val = VMObject.FromObject(temp)

            result.SetKey(key, val)

        return result
    
    @staticmethod
    def FromObject(obj):
        if obj is None:
            # Returns the VMObject equivalent of None
            return VMObject()

        obj_type = type(obj)
        type_enum = VMObject.GetVMType(obj_type)

        if type_enum == VMType.NONE:
            raise Exception("Not a valid object")

        result = VMObject()

        if type_enum == VMType.Bool:
            result.SetValue(bool(obj))
        elif type_enum == VMType.Bytes:
            result.SetValue(bytes(obj), VMType.Bytes)
        elif type_enum == VMType.String:
            result.SetValue(str(obj))
        elif type_enum == VMType.Enum:
            result.SetValue(obj)
        elif type_enum == VMType.Object:
            result.SetValue(obj)
        elif type_enum == VMType.Number:
            result.SetValue(obj)
        elif type_enum == VMType.Timestamp:
            if obj_type == datetime:
                obj = Timestamp(datetime(obj))  # HACK
            result.SetValue(obj)
        elif type_enum == VMType.Struct:
            if isinstance(obj, list):
                return VMObject.FromArray(obj)
        else:
            return None

        return result

    def ToObject(self):
        if self.Type == VMType.NONE:
            raise Exception("Not a valid object")

        if self.Type == VMType.Bool:
            return self.AsBool()
        elif self.Type == VMType.Bytes:
            return self.AsByteArray()
        elif self.Type == VMType.String:
            return self.AsString()
        elif self.Type == VMType.Number:
            return self.AsNumber()
        elif self.Type == VMType.Timestamp:
            return self.AsTimestamp()
        elif self.Type == VMType.Object:
            return self.Data
        elif self.Type == VMType.Enum:
            return self.Data
        elif self.Type == VMType.Struct:
            if not self.IsEmpty:
                return self.Data
            else:
                raise Exception(f"Cannot cast {self.Type} to object")
        else:
            raise Exception(f"Cannot cast {self.Type} to object")

    def ToObjectWithType(self, type):
        if self.Type == VMType.Struct:
            if isinstance(self.Data, list):
                element_type = type.__args__[0]
                return self.ToArray(element_type)
            else:
                return self.ToStruct(type)
        else:
            temp = self.ToObject()
            return temp
        
    def ToArray(self, array_element_type):
        if self.IsEmpty:
            return []

        if self.Type != VMType.Struct:
            raise Exception("Not a valid source struct")

        children = self.GetChildren()
        max_index = -1
        for child in children:
            if child.Key.Type != VMType.Number:
                raise Exception("Source contains an element with an invalid array index")

            temp = child.Key.AsNumber()

            if temp >= 1024:  # TODO: Use a constant for VM max array size
                raise Exception("Source contains an element with a very large array index")

            index = int(temp)
            if index < 0:
                raise Exception("Source contains an array index with a negative value")

            max_index = max(index, max_index)

        length = max_index + 1
        array = [None] * length

        for child in children:
            temp = child.Key.AsNumber()
            index = int(temp)

            val = child.Value.ToObjectWithType(array_element_type)

            val = ConvertObjectInternal(val, array_element_type)

            array[index] = val

        return array
    
    def ToStruct(self, struct_type):
        if self.Type != VMType.Struct:
            raise Exception("Not a valid source struct")

        if not inspect.isclass(struct_type) or not hasattr(struct_type, '__dict__'):
            raise Exception("Not a valid destination struct")

        struct_fields = struct_type.__dict__
        result = struct_type()

        for field_name, field_type in struct_fields.items():
            key = VMObject.FromObject(field_name)

            if key in self.Data:
                val = self.Data[key].ToObjectWithType(field_type)
            else:
                if inspect.isclass(field_type) or inspect.isclass(field_type.__class__):
                    val = None
                else:
                    raise Exception("Field not present in source struct: " + field_name)

            # Here we check if the types mismatch.
            # In case of getting a bytes object instead of an object, we try deserializing the bytes in a different approach.
            # This should not be necessary often.
            if val is not None and field_type != bytes and isinstance(val, bytes):
                if issubclass(field_type, ISerializable):
                    temp = field_type()
                    bytes = val
                    stream = io.BytesIO(bytes)
                    reader = BinaryReader(stream)
                    temp.UnserializeData(reader)
                    val = temp

            # HACK: Allows treating uints as enums, without this it is impossible to transform between C# objects and VM objects.
            if hasattr(field_type, '__enum__') and not isinstance(val, Enum):
                val = field_type(val)

            setattr(result, field_name, val)

        return result
    
    def CastViaReflection(src_obj, level=0, dont_convert_serializables=True):
        src_type = type(src_obj)

        if isinstance(src_obj, pyarray.Array):
            children = {}

            for i, val in enumerate(src_obj):
                key = VMObject()
                key.SetValue(i)
                vm_val = CastViaReflection(val, level + 1)
                children[key] = vm_val

            result = VMObject()
            result.SetValue(children)
            return result
        else:
            target_type = GetVMType(src_type)

            result = None
            is_known_type = src_type in [int, bool, str, bytes, BigInteger, Timestamp]

            if not is_known_type and dont_convert_serializables and issubclass(src_type, ISerializable):
                is_known_type = True

            if is_known_type is False and src_type.__class__.__name__ not in ["type", "EnumMeta"]:
                children = {}

                fields = [attr for attr in dir(src_obj) if not callable(getattr(src_obj, attr)) and not attr.startswith("__")]

                if len(fields) > 0:
                    for field_name in fields:
                        key = VMObject()
                        key.SetValue(field_name)
                        ValidateStructKey(key)

                        val = getattr(src_obj, field_name)
                        vm_val = CastViaReflection(val, level + 1, True)
                        children[key] = vm_val

                    result = VMObject()
                    result.SetValue(children)
                    return result

            if not is_known_type:
                result = VMObject.FromObject(src_obj)
                if result is not None:
                    return result

            raise Exception(f"Invalid cast: Interop.{src_type.__name__} to vm object")
    
    def SerializeData(writer):
        writer.write(bytes([self.Type]))
        
        if self.Type == VMType.NONE:
            return

        data_type = type(self.Data)

        if self.Type == VMType.Struct:
            children = self.GetChildren()
            writer.write_var_int(len(children))
            
            for entry in children:
                entry[0].SerializeData(writer)
                entry[1].SerializeData(writer)
        
        elif self.Type == VMType.Object:
            obj = self.Data
            if isinstance(obj, ISerializable):
                bytes_data = Serialization.Serialize(obj)
                writer.write_byte_array(bytes_data)
            elif isinstance(obj, list):
                writer.write_var_int(len(obj))
                for item in obj:
                    obj2 = CastViaReflection(item, 0, False)
                    obj2.SerializeData(writer)
            else:
                raise Exception(f"Objects of type {data_type.__name__} cannot be serialized")
        
        elif self.Type == VMType.Enum:
            temp2 = int(self.Data) if isinstance(self.Data, Enum) else self.Data
            writer.write_var_int(temp2)
        
        else:
            if self.Type == VMType.String:
                data = self.Data.encode('utf-8')
                writer.write_var_int(len(data))
                writer.write(data)
            elif self.Type == VMType.Number:
                temp1 = str(self.Data)
                temp2 = int(temp1) if isinstance(self.Data, int) else self.Data
                writer.write_var_int(temp2)
            else:
                Serialization.Serialize(writer, self.Data)

    @staticmethod
    def FromBytes(bytes):
        result = VMObject()
        result.UnserializeData(bytes)
        return result

    @staticmethod
    def FromStruct(obj):
        return CastViaReflection(obj, 0, False)
    
    def UnserializeData(bytes_data):
        stream = io.BytesIO(bytes_data)
        reader = BinaryReader(stream)
        self.Type = VMType(reader.read_byte())
        
        if self.Type == VMType.Bool:
            self.Data = Serialization.Unserialize[bool](reader)
            self._localSize = 1
        elif self.Type == VMType.Bytes:
            self.Data = Serialization.Unserialize[bytearray](reader)
            self._localSize = len(self.Data)
        elif self.Type == VMType.Number:
            self.Data = Serialization.Unserialize[bigint](reader)
            self._localSize = 32
        elif self.Type == VMType.Timestamp:
            self.Data = Serialization.Unserialize[Timestamp](reader)
            self._localSize = 8
        elif self.Type == VMType.String:
            self.Data = Serialization.Unserialize[str](reader)
            self._localSize = len(self.Data) if self.Data is not None else 0
        elif self.Type == VMType.Struct:
            child_count = reader.read_var_int()
            self._localSize = child_count if child_count is not None else 0
            children = {}
            
            while child_count > 0:
                key = VMObject()
                key.UnserializeData(reader)
                ValidateStructKey(key)
                
                val = VMObject()
                val.UnserializeData(reader)
                children[key] = val
                child_count -= 1
            
            self.Data = children
        elif self.Type == VMType.Object:
            bytes_data = reader.read_byte_array()
            self._localSize = len(bytes_data) if bytes_data is not None else 0
            
            if len(bytes_data) == 35:
                addr = Serialization.Unserialize[Address](bytes_data)
                self.Data = addr
                self.Type = VMType.Object
            else:
                self.Type = VMType.Bytes
                self.Data = bytes_data
        elif self.Type == VMType.Enum:
            self.Type = VMType.Enum
            self.Data = reader.read_var_int()
            self._localSize = 1
        elif self.Type == VMType.NONE:
            self.Type = VMType.NONE
            self.Data = None
        else:
            raise Exception(f"Invalid unserialize: type {self.Type}")
    
    def __str__(self):
        if self.Type == VMType.String:
            return str(self.Data)
        elif self.Type == VMType.Number:
            return str(self.Data)
        elif self.Type == VMType.Bytes:
            return base64.b64encode(self.Data).decode('utf-8')  # or any other suitable representation
        elif self.Type == VMType.Enum:
            return str(self.Data)
        elif self.Type == VMType.Bool:
            return "true" if self.Data else "false"
        elif self.Type == VMType.Timestamp:
            return str(self.Data)  # Assuming Data holds a datetime object
        elif self.Type == VMType.Struct or self.Type == VMType.Object:
            # Represent Struct or Object as a string (customize as needed)
            return f"Object of type {self.Type} with data: {self.Data}"
        else:
            raise ValueError(f"Invalid cast: expected string, got {self.Type}")
