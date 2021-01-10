from typing import List


class Solution:
  # def hIndex(self, citations: List[int]) -> int:
  #     l = len(citations)
  #     h_index = 0
  #     for i in range(1, l + 1):
  #         count = 0
  #         for c in citations:
  #             if c >= i:
  #                 count += 1
  #         if count < i:
  #             break
  #         else:
  #             h_index = i
  #     return h_index # complexity is O(n^2)


  def hIndex(self, citations: List[int]) -> int:
    l = len(citations)
    tmp = [0] * (l + 1)
    for c in citations:
      i = min(c, l)
      tmp[i] += 1
    res = 0
    for i in range(l, -1, -1):
      res += tmp[i]
      if res >= i:
        return i  # complexity is O(n)

sol = Solution()
print(sol.hIndex([3,0,6,1,5]))