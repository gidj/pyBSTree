class BSTree:
    def __init__(self, head=None):
        pass

    def insert(self, key, value=None):
        pass

    def delete(self, key):
        pass

    def search(self, key):
        pass

class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        # Sometimes the key is the value; if so, payload is just the key
        if value is None:
            self.payload = self.key
        self.left = left
        self.right = right


