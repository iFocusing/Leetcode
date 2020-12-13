class Finder:
  def findKth(self, a, left, right, K):
    # write code here
    i = left
    j = right
    pivot = a[i]

    while i < j:
      while i < j and a[j] <= pivot:  # 从右往左找
        j -= 1
      if i < j:
        a[i] = a[j]

      while i < j and a[i] >= pivot:  # 从左往右找
        i += 1
      if i < j:
        a[j] = a[i]

      a[i] = pivot
      print('pivot', a, i, j, pivot)
      if i + 1 == K:
        print('return', a, i)
        return pivot
      elif i + 1 < K:
        print('right')
        return self.findKth(a, i + 1, right, K - i - 1)
      else:
        print('left')
        return self.findKth(a, left, i - 1, K)
    return r


import sys

# str = input().split(',')
# a, n, K = list(map(int, ','.join(str[:-2])[1:-1].split(','))), int(str[-2]), int(str[-1])
f = Finder()
r = f.findKth([2, 3, 4, 5, 6, 7, 7, 3], 0, 6, 3)
print(r)