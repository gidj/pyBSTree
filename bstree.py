class BSTree:
    def __init__(self, *args, **kwargs):
        self.head = None
        if args:
            print args
            for item in args:
                if type(item) == "tuple":
                    for elem in item:
                        self.insert(elem)
                if type(item) == "list":
                    for elem in item:
                        self.insert(elem)
                if type(item) == "dict":
                    self.insert(*item.items())
                else:
                    self.insert(item)
        if kwargs:
            print kwargs
            for item in kwargs.items():
                self.insert(*item)


    def insert(self, key, value=None):
        if not self.head:
            self.head = Node(key, value)
            return self.head.payload

        cursor = self.head
        while cursor:
            if cursor.key > key:
                if cursor.left:
                    cursor = cursor.left
                else:
                    cursor.left = Node(key, value)
                    return cursor.left.payload
            else:
                if cursor.right:
                    cursor = cursor.right
                else:
                    cursor.right = Node(key, value)
                    return cursor.right.payload

    def search(self, key):
        cursor = self.head
        while cursor:
            if cursor.key == key:
                return cursor.payload
            elif cursor.key > key:
                cursor = cursor.left
            else:
                cursor = cursor.right
        return None

    def delete(self, key):
        pass

class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        # Sometimes the key is the value; if so, payload is just the key
        if value is None:
            self.payload = self.key
        else:
            self.payload = value
        self.left = left
        self.right = right


