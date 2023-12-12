#import big_int  # Assuming big_int is a Python equivalent of big-integer library

class Decoder:
    def __init__(self, str):
        self.str = str

    def is_end(self):
        return len(self.str) == 0

    def read_char_pair(self):
        res = self.str[:2]
        self.str = self.str[2:]
        return res

    def read_byte(self):
        try:
            return int(self.read_char_pair(), 16)
        except ValueError as e:
            # Handle the error or re-raise with a more descriptive message
            raise ValueError(f"read_char_pair() returned an invalid hexadecimal value: {e}")

    def read(self, num_bytes):
        res = self.str[:num_bytes * 2]
        self.str = self.str[num_bytes * 2:]
        return res

    def read_string(self):
        length = self.read_var_int()
        return self.read_string_bytes(length)

    def read_string_bytes(self, num_bytes):
        res = ''
        for _ in range(num_bytes):
            res += chr(self.read_byte())
        return res

    def read_byte_array(self):
        length = self.read_var_int()
        if length == 0:
            return []
        return self.read(length)

    def read_signature(self):
        # Implement as per your signature structure
        pass

    def read_timestamp(self):
        bytes_str = self.read(4)
        result = 0
        for c in reversed([bytes_str[i:i+2] for i in range(0, len(bytes_str), 2)]):
            result = result * 256 + int(c, 16)
        return result

    def read_var_int(self):
        length = self.read_byte()
        res = 0
        if length == 0xfd:
            for c in reversed(self.read(2)):
                res = res * 256 + int(c, 16)
        elif length == 0xfe:
            for c in reversed(self.read(4)):
                res = res * 256 + int(c, 16)
        elif length == 0xff:
            for c in reversed(self.read(8)):
                res = res * 256 + int(c, 16)
        else:
            res = length
        return res

    def read_big_int(self):
        length = self.read_var_int()
        res = 0
        string_bytes = self.read(length)
        for c in reversed([string_bytes[i:i+2] for i in range(0, len(string_bytes), 2)]):
            res = res * 256 + int(c, 16)
        return res

    def read_big_int_accurate(self):
        length = self.read_var_int()
        res = big_int.BigInt()
        string_bytes = self.read(length)
        for c in reversed([string_bytes[i:i+2] for i in range(0, len(string_bytes), 2)]):
            res = res.times(256).plus(int(c, 16))
        return res.toString()

    def read_vm_object(self):
        # Implement as per your VM object structure
        pass
