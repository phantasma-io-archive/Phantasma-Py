from datetime import datetime

class Timestamp:
    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return datetime.utcfromtimestamp(self.value).strftime("%a, %d %b %Y %H:%M:%S GMT")

    def to_string_format(self, format_str: str):
        return datetime.utcfromtimestamp(self.value).strftime(format_str)

    @staticmethod
    def now():
        return int(datetime.now().timestamp())

    @staticmethod
    def null():
        return Timestamp(0)

    def compare_to(self, other):
        if self.value == other.value:
            return 0
        return -1 if self.value < other.value else 1

    def equals(self, obj):
        return isinstance(obj, Timestamp) and self.value == obj.value

    def get_hash_code(self):
        return self.value

    def get_size(self):
        return 4

    @staticmethod
    def equal(A, B):
        return A.value == B.value

    @staticmethod
    def not_equal(A, B):
        return A.value != B.value

    @staticmethod
    def less_than(A, B):
        return A.value < B.value

    @staticmethod
    def greater_than(A, B):
        return A.value > B.value

    @staticmethod
    def less_than_or_equal(A, B):
        return A.value <= B.value

    @staticmethod
    def greater_than_or_equal(A, B):
        return A.value >= B.value

    @staticmethod
    def subtract(A, B):
        return A.value - B.value

    @staticmethod
    def from_number(ticks):
        return Timestamp(ticks)

    @staticmethod
    def from_date(time):
        return Timestamp(int(time.timestamp()))

    @staticmethod
    def add_time_span(A, B):
        return A.value + B

    @staticmethod
    def subtract_time_span(A, B):
        return A.value - B

    # Serialize and Unserialize methods are placeholders
    @staticmethod
    def Serialize():
        pass

    @staticmethod
    def Unserialize():
        pass