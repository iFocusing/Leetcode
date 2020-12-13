from typing import List


class Solution:
  """
  Given a non-empty array nums containing only positive integers, find if the array can be partitioned
  into two subsets such that the sum of elements in both subsets is equal.
  """
  def canPartition(self, nums: List[int]) -> bool:
    # dp 2-D matrix
    # s = sum(nums)
    # if s % 2 != 0 or len(nums) < 2:
    #     return False
    # c = s // 2
    # n = len(nums)
    # dp = [[0 for i in range(c + 1)] for j in range(n + 1)]
    # for i in range(1, n + 1):
    #     for j in range(1, c + 1):
    #         dp[i][j] = dp[i-1][j]
    #         if j >= nums[i - 1] and dp[i][j] < dp[i-1][j-nums[i-1]] + nums[i-1] <= c:
    #             dp[i][j] = dp[i-1][j-nums[i-1]] + nums[i-1]
    # if dp[-1][-1] == c:
    #     return True
    # else:
    #     return False

    # dp 1-D list
    s = sum(nums)
    n = len(nums)
    if s % 2 != 0 or n < 2:
      return False
    c = s // 2
    dp = [False for i in range(c + 1)]
    if nums[0] <= c:
      dp[nums[0]] = True
    for i in range(1, n):
      for j in range(c, 0, -1):
        if j >= nums[i]:
          dp[j] = dp[j] or dp[j - nums[i]]
    return dp[c]



sol = Solution()
print(sol.canPartition([1,5,11,5]))
