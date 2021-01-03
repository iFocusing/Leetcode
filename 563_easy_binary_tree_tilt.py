from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  """
  Given the root of a binary tree, return the sum of every tree node's tilt.
  """

  def findTilt(self, root: TreeNode) -> int:
    # depth-first search (BFS) using post-order
    node_tilt = []

    def helper(node):
      # return the sum of all values in a sub-tree
      if node is None:
        return 0
      l = helper(node.left)
      r = helper(node.right)
      node_tilt.append(abs(l - r))
      return node.val + l + r

    helper(root)
    return sum(node_tilt)


  def read_tree(self, tree: List):
    # breadth-first search (BFS)
    root = TreeNode(tree[0])
    nodes = []
    nodes.append(root)
    l = len(tree)
    i = 1
    while i < l:
      current_node = nodes[0]
      current_node.left = TreeNode(tree[i]) if tree[i] is not None else None
      current_node.right = TreeNode(tree[i + 1]) if tree[i+1] is not None else None
      nodes.append(current_node.left)
      nodes.append(current_node.right)
      i += 2
      nodes.pop(0)
    return root


sol = Solution()
tree = [21,7,14,1,1,2,2,3,3]
print(sol.findTilt(sol.read_tree(tree)))