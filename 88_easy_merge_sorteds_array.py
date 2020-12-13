from typing import List


class Solution:
  """
  Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

  Note:

  The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
  """
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if n == 0:
      return nums1
    i = m - 1
    j = n - 1
    current = m + n - 1
    while i >= 0 and j >= 0:
      if nums1[i] >= nums2[j]:
        nums1[current] = nums1[i]
        i -= 1
      else:
        nums1[current] = nums2[j]
        j -= 1
      current -= 1
    while j >= 0:
      nums1[current] = nums2[j]
      current -= 1
      j -= 1
    return nums1

sol = Solution()
print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))