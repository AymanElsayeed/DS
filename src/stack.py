"""

    Stack Class

    implement Stack using python list builtin data structure

"""


class Stack:
    def __init__(self):
        self.items: list = []

    def push(self, item):
        """
        Push an item in the top of stack, the run time O(1)
        :param item:
        :return:
        """
        self.items.append(item)

    def pop(self):
        """
        Get and remove the last item added to the stack, the run time O(1)
        return None if the stack is empty
        :return: item
        :rtype: object
        """
        return self.items.pop() if self.items else None

    def peek(self):
        """
        Shows without remove the last item added to the stack,None if the stack is empty the run time O(1)
        :return: item
        :rtype: object
        """
        return self.items[-1] if self.items else None

    def size(self):
        """
        The size/length of the stack, run in constant time
        :return: number of items in the stack
        :rtype: int
        """
        return len(self.items)

    def is_empty(self):
        """
        Whether the stack is empty or not, run in constant time
        :return: boolean value
        :rtype: bool
        """
        return self.size() == 0
