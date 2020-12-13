# Definition for a binary tree node.
from typing import List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  """
  Given the root of a binary tree, determine if it is a valid binary search tree (BST).

  A valid BST is defined as follows:

  The left subtree of a node contains only nodes with keys less than the node's key.
  The right subtree of a node contains only nodes with keys greater than the node's key.
  Both the left and right subtrees must also be binary search trees.
  """
  def isValidBST(self, root: TreeNode) -> bool:
    def helper(node, lower=float('-inf'), upper=float('inf')):
      if node is None:
          return True
      if node.val <= lower or node.val >= upper:
          return False
      if not helper(node.right, node.val, upper):
          return False
      if not helper(node.left, lower, node.val):
          return False
      return True
    return helper(root)

  def bulid(self, l: List[int]):
    expand = []
    head = TreeNode(l[0])
    expand.append(head)
    if len(l) == 1:
      return head
    i = 0
    while i < len(l) - 2:
      i += 1
      node = TreeNode(l[i])
      expand.append(node)
      expand[0].left = node

      i += 1
      node = TreeNode(l[i])
      expand.append(node)
      expand[0].right = node

      expand.pop(0)
    return head


sol = Solution()
print(sol.isValidBST(sol.bulid([5,1,4,"null","null",3,6])))