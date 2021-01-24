class Solution:
  def totalNQueens(self, n: int) -> int:
    self.res = 0
    self.n = n
    self.dfs(0, [], [], [])
    return self.res

  def dfs(self, row, cols, left_diag, right_diag):
    # dfs, recursion
    if row == self.n:
      self.res += 1
    for col in range(self.n):
      if col in cols or (row + col) in left_diag or (row - col) in right_diag:
        continue
      self.dfs(row + 1,
               cols + [col],
               left_diag + [row + col],
               right_diag + [row - col])
