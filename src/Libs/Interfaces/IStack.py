class IStack:
    def __init__(self):
        self._stack = []

    def push(self, item):
        """
        Push an item onto the stack.
        """
        self._stack.append(item)

    def pop(self):
        """
        Pop an item off the stack.
        """
        return self._stack.pop() if self._stack else None

    def peek(self):
        """
        Peek at the top item of the stack without removing it.
        """
        return self._stack[-1] if self._stack else None

    def size(self):
        """
        Get the number of items in the stack.
        """
        return len(self._stack)