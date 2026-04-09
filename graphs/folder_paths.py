# https://interviewing.io/questions/print-folder-structure

# The Print Folder Structure problem asks us to take an input of file paths and print out the files in each folder.
# Input : Input: files = [ "/webapp/assets/html/a.html", "/webapp/assets/html/b.html", "/webapp/assets/js/c.js", "/webapp/index.html" ]

# Iterate through each element in the files array
# Split the string based on "/". If there is a '.' in the string, it's a leaf ?
# Create a node with child nodes (maybe an array).
# Insert a node : if the root is already present, traverse until a new node has to be created.


class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}


class Tree:
    def __init__(self):
        self.root = Node("")

    def insert_node(self, folder_path):
        folders = folder_path.split("/")[1:]
        node = self.root
        for folder in folders:
            if folder not in node.children:
                node.children[folder] = Node(folder)
            node = node.children[folder]

    def print_files(self):
        self._dfs_print(self.root, "")

    def _dfs_print(self, node, indent):
        if not node.children:
            print(indent + "-- " + node.name)
            return
        print(indent + "-- " + node.name)
        for child in node.children.values():
            self._dfs_print(child, indent + " ")


# Test case
files = [
    "/webapp/assets/html/a.html",
    "/webapp/assets/html/b.html",
    "/webapp/assets/js/c.js",
    "/webapp/index.html"
]
tree = Tree()
for file in files:
    tree.insert_node(file)

tree.print_files()
