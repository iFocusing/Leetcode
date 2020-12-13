
from typing import List


class Solution(object):
  def canThreePartsEqualSum(self, A: List[int]):
    """
    :type A: List[int]
    :rtype: bool
    """
    partition = sum(A) / 3
    count = 0
    part = 0

    if sum(A) % 3 != 0 or len(A) < 3:
      return False
    else:
      for i in range(len(A) - 1):
        part = part + A[i]
        if part == partition:
          count = count + 1
          part = 0
          if count == 2:
            return True
      return False

sol = Solution()
print(sol.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))