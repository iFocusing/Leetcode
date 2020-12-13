from typing import List


class Solution:
  def sortArray(self, nums: List[int]) -> List[int]:
    return self.q_sort(nums, 0, len(nums) - 1)

  def q_sort(self, L, left, right):
    if left < right:
      pivot = self.Partition(L, left, right)

      self.q_sort(L, left, pivot - 1)
      self.q_sort(L, pivot + 1, right)
    return L

  def Partition(self, L, left, right):
    pivotkey = L[left]

    while left < right:
      while left < right and L[right] >= pivotkey:
        right -= 1
      L[left] = L[right]
      while left < right and L[left] <= pivotkey:
        left += 1
      L[right] = L[left]

    L[left] = pivotkey
    return left


sol = Solution()
print(sol.sortArray([5,1,1,2,0,0]))