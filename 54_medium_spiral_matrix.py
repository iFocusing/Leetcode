from typing import List


class Solution:
  """
  Given an m x n matrix, return all elements of the matrix in spiral order.
  """
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    res = []
    r, c = len(matrix), len(matrix[0])
    seen = [[False for _ in range(c)] for _ in range(r)]
    print(seen)
    x_steps = [0, 1, 0, -1]
    y_steps = [1, 0, -1, 0]
    x = y = s = 0
    for _ in range(r * c):
      res.append(matrix[x][y])
      seen[x][y] = True
      xt = x + x_steps[s]
      yt = y + y_steps[s]
      if 0 <= xt < r and 0 <= yt < c and not seen[xt][yt]:
        x = xt
        y = yt
      else:
        s = (s + 1) % 4
        x += x_steps[s]
        y += y_steps[s]
    return res

