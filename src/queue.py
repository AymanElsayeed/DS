"""

    Queue Class

    implement Queue using python list builtin data structure

"""


class Queue:
    def __init__(self):
        self.items: list = []

    def enqueue(self, item):
        """
        add item to the head of the queue, run in constant time
        :param item:
        :return: None
        :rtype None
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        return and remove the front-most item of the queue, run in constant time
        :return:
        :rtype: object
        """
        return self.items.pop() if self.items else None

    def peek(self):
        """
        Return the last (front-most) item without remove it in the queue, run in constant time
        :return:
        :rtype object
        """
        return self.items[-1] if self.items else None

    def size(self):
        """
        Return the size of the queue, run in constant time
        :return: size
        :rtype: int
        """
        return len(self.items)

    def is_empty(self):
        """
        Whether the queue is empty or not, run in constant time
        :return:
        """
        return self.size() == 0
