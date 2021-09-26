from tree import Node

root = Node("root")
right = Node("right")
left = Node("left")
lr = Node("lr")
ll = Node("ll")
root.right = right
root.left = left
left.right = lr
left.left = ll
print("\n")
root.print_subtrees()
print("\n")