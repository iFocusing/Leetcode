class Solution(object):

  def solveNQueens(self, n):
    self.sols = []
    self.n = n
    self.dfs(0, [], [], [])
    return self.sols

  def dfs(self, row, cols, left_diag, right_diag):
    # dfs, recursion
    if row == self.n:
      sol = ['.' * col + 'Q' + '.' * (self.n - 1 - col) for col in cols]
      self.sols.append(sol)
      return
    for col in range(self.n):
      if col in cols or (row + col) in left_diag or (row - col) in right_diag:
        continue
      self.dfs(row + 1,
               cols + [col],
               left_diag + [row + col],
               right_diag + [row - col])
