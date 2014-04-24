import collections

class BSTree:
    def __init__(self, *args, **kwargs):
        self.head = None
        if args:
            print args
            for item in args:
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
        """ Takes a key, finds the node associated with that key and returns the
        value of the deleted key after deleting the node and maintaining the 
        search structure of the tree"""
        pass

    def print_in_order(self):
        if self.head is None:
            return []
        else:
            return self.head.print_in_order()

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

    def print_in_order(self):
        sublist = []
        if self.left:
            sublist.extend(self.left.print_in_order())
        sublist.append(self.payload)
        if self.right:
            sublist.extend(self.right.print_in_order())
        return sublist

