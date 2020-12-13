from typing import List


class Solution:
  """
  Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.
  """
  def numSubmat(self, mat: List[List[int]]) -> int:
    rows = len(mat)
    cols = len(mat[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    #dp[i][j]表示第i行，从j开始往左数连续有多少个1
    for i in range(rows):
      for j in range(cols):
        if mat[i][j]:
            dp[i][j] = dp[i][j-1] + 1 if j > 0 else 1
    res = 0
    #遍历每个位置，以这个位置为矩形右下角
    for i in range(rows):
      for j in range(cols):
        #leftnum维护可以构成矩形的最大宽度
        leftnum = float('inf')
        #从(i,j)开始向上遍历，对于第i行，求出dp(i,j)表示(i,j)左边的连续1个数
        #也就是以(i,j)为右下角，高为1，的矩形个数(一个长度对应一个矩形)
        #遍历到i-1行的时候，更新leftnum，表示第i行和第i-1行从j往左的连续1的个数的
        #较小值，这就是以(i,j)为右下角，高为2的矩形个数
        #遍历i上面的所有行，找到所有的(i,j)为右下角，高度分别为1,2,3...，i+1的矩形
        for k in range(i,-1,-1):
          leftnum = min(leftnum,dp[k][j])
          #如果某一行更新后，leftnum为0，那么上面的行就不用看了，break跳出
          if leftnum == 0:
            break
          res += leftnum
    return res


sol = Solution()
print(sol.numSubmat(
              [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]))
