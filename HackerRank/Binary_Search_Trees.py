# Binary Tree

# Fundamentally, a binary tree is composed of nodes connected by edges (with further restrictions discussed below). Some binary tree,
# t, is either empty or consists of a single root element with two distinct binary tree child elements known as the left subtree and
# the right subtree of t. As the name binary suggests, a node in a binary tree has a maximum of 2 children.

# Here are the basic facts and terms to know about binary trees:

# - The convention for binary tree diagrams is that the root is at the top, and the subtrees branch down from it.
# - A node's left and right subtrees are referred to as children, and that node can be referred to as the parent of those subtrees.
# - A non-root node with no children is called a leaf.
# - Some node a is an ancestor of some node b if b is located in a left or right subtree whose root node is a. This means that the 
# root node of binary tree is the ancestor of all other nodes in the tree.
# - If some node is an ancestor of some node , then the path from to is the sequence of nodes starting with , moving down the 
# ancestral chain of children, and ending with .
# - The depth (or level) of some node is its distance (i.e., number of edges) from the tree's root node.
# - Simply put, the height of a tree is the number of edges between the root node and its furthest leaf. More technically put, it's 
# (i.e., one more than the maximum of the heights of its left and right subtrees). Any node has a height of , and the height of an 
# empty subtree is . Because the height of each node is the maximum height of its subtrees and an empty subtree's height is , the 
# height of a single-element tree or leaf node is .


# Task
# The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. You are given a pointer,
# root, pointing to the root of a binary search tree. Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.

# Input Format
# The locked stub code in your editor reads the following inputs and assembles them into a binary search tree:
# The first line contains an integer, n, denoting the number of nodes in the tree.
# Each of the n subsequent lines contains an integer, data, denoting the value of an element that must be added to the BST.

# Output Format
# The locked stub code in your editor will print the integer returned by your getHeight function denoting the height of the BST.

# Sample Input
# 7
# 3
# 5
# 2
# 1
# 4
# 6
# 7

# Sample Output
# 3

# ====================================================================================================
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        if root == None:
            return -1
        else:
            return 1 + max( self.getHeight(root.left), self.getHeight(root.right) )

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)   
