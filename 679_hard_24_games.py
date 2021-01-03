from typing import List


class Solution:
  def judgePoint24(self, nums: List[int]) -> bool:
    if len(nums) == 1 and nums[0] == 24:
      return True
    elif len(nums) == 1 and nums[0] != 24:
      return False
    operations = ['+', '-1', '-2', '*', '/1', '/2']
    l = len(nums)
    for i in range(l):
      for j in range(i + 1, l):  # iterate every two cards
        tmp = nums.copy()
        a = nums[i]
        b = nums[j]
        tmp.remove(a)
        tmp.remove(b)
        print('i,j:', i, j, nums, tmp, a, b)
        for opt in operations:  # for each card pair, iterate every operation
          tmp2 = tmp.copy()
          print(tmp, tmp2, a, opt, b)
          if opt == '+':
            tmp2.append(a + b)
          elif opt == '-1':
            tmp2.append(a - b)
          elif opt == '-2':
            tmp2.append(b - a)
          elif opt == '*':
            tmp2.append(a * b)
          elif opt == '/1' and b != 0:
            tmp2.append(a / b)
          elif opt == '/2' and a != 0:
            tmp2.append(b / a)

          if self.judgePoint24(tmp2):
            return True

    return False

sol = Solution()
print(sol.judgePoint24([3,3,8,8]))