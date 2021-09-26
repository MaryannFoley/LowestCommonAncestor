class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def print_subtrees(self, indentation = ""):
        if self.right:
            self.right.print_subtrees(indentation = indentation+"\t")
        print(indentation+self.data)
        if self.left:
            self.left.print_subtrees(indentation = indentation+"\t")
