import queue
from sys import stdin, setrecursionlimit


setrecursionlimit(10 ** 6)

#Following the structure used for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




def getSum(root):
    if root is None:
        return 0
    leftSum = getSum(root.left)
    rightSum = getSum(root.right)
    return root.data + leftSum + rightSum


