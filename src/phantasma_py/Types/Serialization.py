import struct
import io
import inspect
from typing import Callable, Any, Type


# TODO: Implement the Serialization class
class Serialization:
    _custom_serializers = {}  # Dictionary to store custom serializers

    @staticmethod
    def register_type(cls: Type, reader: Callable, writer: Callable):
        Serialization._custom_serializers[cls] = (reader, writer)

    @staticmethod
    def serialize(obj: Any) -> bytes:
        if obj is None:
            return b''

        # Check for custom serialization
        if type(obj) in Serialization._custom_serializers:
            writer = Serialization._custom_serializers[type(obj)][1]
            stream = io.BytesIO()
            writer(stream, obj)
            return stream.getvalue()

        # Handle basic types
        if isinstance(obj, bool):
            return struct.pack('?', obj)
        elif isinstance(obj, int):
            return struct.pack('<i', obj)
        # ... other basic types ...

        # Handle complex objects
        # This would require a more complex implementation
        # ...

        raise ValueError(f"Unsupported type: {type(obj)}")

    @staticmethod
    def unserialize(data: bytes, cls: Type) -> Any:
        if not data:
            return None

        # Check for custom deserialization
        if cls in Serialization._custom_serializers:
            reader = Serialization._custom_serializers[cls][0]
            stream = io.BytesIO(data)
            return reader(stream)

        # Handle basic types
        if cls == bool:
            return struct.unpack('?', data)[0]
        elif cls == int:
            return struct.unpack('<i', data)[0]
        # ... other basic types ...

        # Handle complex objects
        # This would require a more complex implementation
        # ...

        raise ValueError(f"Unsupported type: {cls}")

    # ... other methods ...
