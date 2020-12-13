import math
from typing import List


class Solution:
  """
  You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
  Design an algorithm to find the maximum profit. You may complete at most k transactions.
  """
  def maxProfit(self, k: int, prices: List[int]) -> int:
    # at most k transactions.
    # prices[i]
    if not prices or k <= 0: return 0
    dp = [[[-math.inf, -math.inf] for i in range(k + 1)] for _ in range(len(prices))]  # consider the case of k = 0
    dp[0][0][1] = 0
    dp[0][1][0] = -prices[0]
    # the first element in the third dimension dp[*][*][0] stores the value if there are stocks at hand;
    # dp[*][*][1] stores the value if there are not stocks at hand;
    for i in range(1, len(prices)):
      for j in range(k + 1):
        if j > 0:
          dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] - prices[i])  # buying
        dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] + prices[i])  # selling
    return max(dp[len(prices) - 1][j][1] for j in range(k + 1))


sol = Solution()
print(sol.maxProfit(2, [2, 4, 1]))

