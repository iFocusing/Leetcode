class Solution(object):
  def maximalRectangle(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if matrix == None or len(matrix) == 0:
      return 0
    height = [0 for i in range(len(matrix[0]))]
    ans = 0
    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        if matrix[i][j] == "0":
          height[j] = 0
        else:
          height[j] += 1
      res = self.maxRectange(height)
      ans = max(ans, res)
    return ans

  def maxRectange(self, height):
    ans = 0
    stack = []
    for i in range(len(height) + 1):
      cur = height[i] if i < len(height) else -1
      if len(stack) == 0 or cur >= height[stack[-1]]:
        stack.append(i)
      else:
        while len(stack) != 0 and cur < height[stack[-1]]:
          h = height[stack.pop()]
          left = stack[-1] if len(stack) != 0 else -1
          area = h * (i - left - 1)
          ans = max(area, ans)
        stack.append(i)
    return ans

sol = Solution()
print(sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))