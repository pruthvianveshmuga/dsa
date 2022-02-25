# https://leetcode.com/problems/range-sum-of-bst/

import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS with stack
def solution2(root: TreeNode, low, high):
    stack = [root]
    ans = 0
    while stack:
        node = stack.pop()
        if not node:
            continue
        if node.val < low:
            stack.append(node.right)
        elif node.val > high:
            stack.append(node.left)
        else:
            ans += node.val
            stack.append(node.right)
            stack.append(node.left)
    return ans

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
