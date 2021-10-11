from tree import Node

def lowest_common_ancestor_helper(node1, node2, currentNode):
    if node1==node2:
        return 2, node1
    numFound = 0
    if currentNode.left:
        lNumFound,lNode = lowest_common_ancestor_helper(node1,node2,currentNode.left)
        if lNumFound == 2:
            return 2, lNode
        numFound += lNumFound
    if currentNode.right:
        rNumFound,rNode = lowest_common_ancestor_helper(node1,node2,currentNode.right)
        if rNumFound == 2:
            return 2, rNode
        numFound += rNumFound
    if currentNode == node1 or currentNode == node2:
        numFound += 1
    #print (numFound, currentNode.data)
    return numFound, currentNode

def lowest_common_ancestor(node1, node2, root):
    numFound, node = lowest_common_ancestor_helper(node1, node2, root)
    return node.data





def test_tree_creation():
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

    print(lowest_common_ancestor(ll, ll, root))
