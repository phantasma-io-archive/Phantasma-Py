from abc import ABC, abstractmethod

# Assuming PBinaryReader and PBinaryWriter are defined elsewhere in your Python code
# from p_binary_reader import PBinaryReader
# from p_binary_writer import PBinaryWriter

class ISerializable(ABC):
    @abstractmethod
    def serialize_data(self, writer: 'PBinaryWriter'):
        """
        Serialize the object data using the provided binary writer.
        """
        pass

    @abstractmethod
    def unserialize_data(self, reader: 'PBinaryReader'):
        """
        Unserialize the object data using the provided binary reader.
        """
        pass