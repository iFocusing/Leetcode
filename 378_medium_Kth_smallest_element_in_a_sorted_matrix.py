from typing import List

class Solution:
  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    # 1. Complexity: n^2 * log n
    # return sorted(sum(matrix, []))[k-1]

    # 2. merge n sorted lists
    # res = matrix[0]
    # for i in range(1, len(matrix)):
    #     res = self.merge_sorted(res + [0] * len(matrix), matrix[i])
    # return res[k-1]

    # 3. binary search
    smallest = matrix[0][0]
    largest = matrix[-1][-1]
    while smallest < largest:
      middle = (smallest + largest) // 2
      i = len(matrix) - 1
      j = 0
      count = 0
      while i >= 0 and j < len(matrix[0]):
        if matrix[i][j] <= middle:
          count += i + 1
          j += 1
        else:
          i -= 1
      if count < k:
        smallest = middle + 1
      else:
        largest = middle
    return smallest

  def merge_sorted(self, l1, l2):
    m, n = len(l1), len(l2)
    i = m - n - 1
    j = n - 1
    current = m - 1
    while i >= 0 and j >= 0:
      if l1[i] >= l2[j]:
        l1[current] = l1[i]
        i -= 1
      else:
        l1[current] = l2[j]
        j -= 1
      current -= 1
    while j >= 0:
      l1[current] = l2[j]
      j -= 1
      current -= 1
    return l1


sol = Solution()
print(sol.kthSmallest([
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]], 8))
