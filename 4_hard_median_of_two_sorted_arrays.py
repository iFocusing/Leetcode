from typing import List


class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    m = len(nums1)
    n = len(nums2)
    # assume nums1 is the shorter list with size m, i.e. m < n
    if m > n:
      m, n, nums1, nums2 = n, m, nums2, nums1
    if m == 0 and n != 0:
      if n % 2 == 0:
        return (nums2[round(n / 2) - 1] + nums2[round(n / 2)]) / 2
      else:
        return nums2[round(n / 2)]
    elif n == 0:
      raise ValueError
    search_range_low = 0
    search_range_high = m
    print(m, n, search_range_low, search_range_high)
    while search_range_low <= search_range_high:
      nums1_i = (search_range_low + search_range_high) // 2
      nums2_j = (m + n + 1) // 2 - nums1_i
      print(m, n, search_range_low, search_range_high, nums1_i, nums2_j)
      if nums1_i < m and nums1[nums1_i] < nums2[nums2_j - 1]:
        print('1')
        # if the next element in the nums1 is still smaller than the current element in the nums2, then the nums1_i is too small
        search_range_low += 1
      elif nums1_i > 0 and nums1[nums1_i - 1] > nums2[nums2_j]:
        print('2')
        # if the current element in the nums1 is already larger than the next element in the nums2, then the nums1_i is too large
        search_range_high -= 1
      else:
        print('3')
        if nums1_i == 0:
          left = nums2[nums2_j - 1]
        elif nums2_j == 0:
          left = nums1[nums1_i - 1]
        else:
          left = max(nums1[nums1_i - 1], nums2[nums2_j - 1])

        if nums1_i == m:
          right = nums2[nums2_j]
        elif nums2_j == n:
          right = nums1[nums1_i]
        else:
          right = min(nums1[nums1_i], nums2[nums2_j])

        print('left, right:', left, right)
        if (m + n) % 2 == 1:
          return left
        else:
          return (left + right) / 2


sol = Solution()
print(sol.findMedianSortedArrays([1, 2], [3, 4]))
