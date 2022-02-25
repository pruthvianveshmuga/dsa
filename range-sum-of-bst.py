# https://leetcode.com/problems/range-sum-of-bst/

import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS - time O(n), space O(n) where n is the number of nodes in the tree
def solution1(root: TreeNode, low, high):
    ans = 0
    def search(node: TreeNode):
        if node == None:
            return
        nonlocal ans
        if node.val < low:
            search(node.right)
        elif node.val > high:
            search(node.left)
        else:
            ans += node.val
            search(node.left)
            search(node.right)

    search(root)
    return ans
