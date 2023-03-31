class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    def print_BST(self):
        if self.left:
            self.left.print_BST()
        print(self.value, end=" ")
        if self.right:
            self.right.print_BST()


# 1 2 5 5 10 12 13 14 15 22
root = BST(10)
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(5)
root.insert(1)
root.insert(13)
root.insert(22)
root.insert(12)
root.insert(14)

root.print_BST()
print("\n")
if root.contains(13):
    print("True")
else:
    print("False")