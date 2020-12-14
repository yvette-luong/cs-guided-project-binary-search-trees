"""
Let's implement a binary search tree class with `insert`
and `search` methods.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


'''
Inserts the input value into our BST
Doesn't return anything ​
Base case: Stop recursing when we find an
empty spot in the tree to place the value
How do we move closer to the base case? At each
node in the BST, compare the current node's value
against the input value. Decide if we go left or
right. If there's already a child node in the direction
we need to go in, continue recursing.
Duplicate values on the right side.
'''


    def insert(self, value):
    # when we were working with linked lists, we kept a
    # variable called `current` to keep track of where we
    # were as we traversed the linked list
    # `self` represents the current node we on as we traverse

       # if we don't want to allow duplicates
       # if value == self.value:
        #     return
       # let's compare the input value against `self`
        if value < self.value:
            # go left
            # check if there is a child node in the left direction
            # there's a node in the direction we need to go in
            if self.left is not None:
                # we need to recurse in the left direction
                self.left.insert(value)
            # there's no node in the direction we need to go in
            else:
                # we can park the value in that spot
                self.left = BSTNode(value)
        else:
            # go right
            # check if there is a child node in the right direction
            if self.right is not None:
                # there's a node in the direction we need to go in
                self.right.insert(value)
            # there's no node in the direction we need to go in
            else:
                # we can park the value in that spot
                self.right = BSTNode(value)


'''
Input: target that we're searching for in the BST
Output: returns a boolean indicating if the target
is in the BST
Base case(s):
1. We found a node whose value matches our target
2. We didn't find what we're looking for. If we find
an empty spot where the value should be, then the value
doesn't exist in our tree.
How do we get closer to a base case?
Compare the target against the current node's value
to determine which direction to go in.
'''

    def search(self, target):
       # check if the current node's value matches target
        if self.value == target:
            return True
​
        elif target < self.value:
            # go left
            # check if the left child is empty or not
            if self.left is None:
            # the target doesn't exist in our tree
                return False

            else:
            # there is a child node in this direction
            # recurse on that child node
                return self.left.search(target)
​
        else:
            # go right
            # check if the right child is empty or not
            if self.right is None:
            # the target doesn't exist in our tree
                return False
            else:
            # there is a child node in this direction
            # recurse on that child node
            return self.right.search(target)


bst.insert(18)
bst.insert(47)
bst.insert(14)
bst.insert(22)
bst.insert(35)
bst.insert(55)
bst = BSTNode(2)
bst.insert(14)
bst.insert(18)
bst.insert(22)
bst.insert(35)
bst.insert(47)
bst.insert(55)
​
print(bst.search(35))
print(bst.search(22))
print(bst.search(55))
print(bst.search(101))
