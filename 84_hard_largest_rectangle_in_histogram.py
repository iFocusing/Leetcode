
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
# 输入: [2,1,5,6,2,3]
# 输出: 10

class Solution(object):
  def largestRectangleArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    if height == None:
      return 0
    stack = []
    # 添加-1是为了判断是不是进行到了最后一个
    height.append(-1)
    ans = 0
    for i in range(len(height)):
      cur = height[i]
      # 如果栈为空或者当前柱比栈顶柱要高，入栈
      if len(stack) == 0 or cur >= height[stack[-1]]:
        stack.append(i)
      else:
        # 如果栈不为空并且当前柱比栈顶柱要低，出栈，更新结果。
        while len(stack) != 0 and cur <= height[stack[-1]]:
          h = height[stack.pop()]
          left = stack[-1] if len(stack) != 0 else -1
          ans = max(ans, h * (i - left - 1))
        stack.append(i)
    return ans

sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))