from typing import List

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    numdict = dict()
    for n in nums:
      if n in numdict:
        numdict[n] += 1
      else:
        numdict[n] = 1
    res = sorted(numdict.items(), key=lambda item: item[1], reverse=True)
    return [res[i][0] for i in range(k)]

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3,3,3,3,3], 2))