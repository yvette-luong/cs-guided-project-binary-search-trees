"""
You are given a binary tree.

Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.

Example:

Given the following binary tree

    5
   / \
  12  32
     /  \
    8    4

your function should return the depth = 3.
"""
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxDepth(self, root):
    # Your code here
    '''
    Input: root node of the binary tree 
    we want to find the max depth for 
    Output: integer representing the max depth

    In this case, this is not a question
    about the values contained in the nodes.
    Instead, we're trying to figure out something
    about the structure of the tree. 
    One idea is to go through all the possible 
    paths from root to leaf nodes, getting 
    their depths in the process, and figuring
    out which one is the max depth.

    Base case: check a node, if there's nothing
    there, that's a depth of 0 

    How do we move closer to a base case? 
    Recurse in both its left and right directions
    Both recursive calls are going to come back
    with answers from further down the tree.
    We'll need to get the max of those returned
    values and then add 1 to account for the 
    current node itself. 
    '''
    # checking if the current node is empty
    if root is None:
        return 0 

    # the root node is not empty 
    # recurse on the left and right sides 
    # to find their respective depths 
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
    # add 1 to account for this current node
        answer = max(left_depth, right_depth) + 1
    return answer

# Creating the binary tree in the above example

left = BinaryTreeNode(12)
right = BinaryTreeNode(32, BinaryTreeNode(8), BinaryTreeNode(4))
root = BinaryTreeNode(5, left, right)

print(maxDepth(root))

