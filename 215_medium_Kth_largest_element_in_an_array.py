from typing import List

class Solution:
  """
  Find the kth largest element in an unsorted array.
  Note that it is the kth largest element in the sorted order, not the kth distinct element.
  """
  def findKthLargest(self, nums: List[int], k: int) -> int:
    return self.findKth(nums, 0, len(nums) - 1, k)

  def findKth(self, a, left, right, K):
    i = left
    j = right
    pivot = a[i]

    while i < j:
      while i < j and a[j] <= pivot:  # 从右往左找
        j -= 1
      a[i] = a[j]

      while i < j and a[i] >= pivot:  # 从左往右找
        i += 1
      a[j] = a[i]
    a[i] = pivot

    if i + 1 == K:
      return pivot
    elif i + 1 < K:
      return self.findKth(a, i + 1, right, K)
    else:
      return self.findKth(a, left, i - 1, K)
    return r

  # import sys
  # str = input().split(',')
  # a, n, K = list(map(int, ','.join(str[:-2])[1:-1].split(','))), int(str[-2]), int(str[-1])
  # f = Finder()
  # r = f.findKthLargest(a, 0, n - 1, K)
  # print(r)

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))