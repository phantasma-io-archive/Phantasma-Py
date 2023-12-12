class Stack:
    def __init__(self, capacity=float('inf')):
        self.storage = []
        self.capacity = capacity

    def push(self, item):
        if self.size() == self.capacity:
            raise Exception("Stack has reached max capacity, you cannot add more items")
        self.storage.append(item)

    def pop(self):
        return self.storage.pop() if self.storage else None

    def peek(self):
        return self.storage[-1] if self.storage else None

    def size(self):
        return len(self.storage)

    def is_empty(self):
        return self.size() == 0

    def to_array(self):
        return self.storage.copy()

    def clear(self):
        self.storage = []

    def __str__(self):
        return str(self.storage)

    def is_full(self):
        return self.capacity == self.size()