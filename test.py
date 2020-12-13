import sys
# for line in sys.stdin:
#   line = list(map(int, sys.stdin.readline().strip().split()))

# n = int(sys.stdin.readline().strip())

# while True:
#   try:
#     pass
#   except:
#     break

# if __name__ == "__main__":
#   main()

# ===========================================================================
# string = 'abc'
# print(string)
# if len(string)== 0:
#     print('')
# n = len(string) // 8
# for i in range(n):
#     print(string[8*i:8*(i+1)])
# if len(string) > n * 8:
#     print(string[n*8:] + ''.join([str(0)]*(8*(n+1)-len(string))))
#
# ===========================================================================
#
# num = 93938
# res, left, right =[], 1, num
# for i in range(2, int(num**0.5)):
#     while right % i == 0:
#         res.append(str(i))
#         right /= i
#         left *= i
# print(left, right)
# if left != num and int(num/left) != num:
#     res.append(str(int(num/left)))
# print(' '.join(res) + ' ' if len(res) != 0 else str(num) + ' ')
#
# ===========================================================================
#
# while True:
#   try:
#     n = int(sys.stdin.readline().strip())
#     res = dict()
#     for i in range(n):
#       line = list(map(int, sys.stdin.readline().strip().split()))
#       if res.get(line[0]) is not None:
#         res[line[0]] += line[1]
#       else:
#         res[line[0]] = line[1]
#     res = sorted(res.items(), key=lambda x: x[0])
#     for item in res:
#       print(str(item[0]), str(item[1]))
#   except:
#     break
# ===========================================================================

# num = '123243245345'
# if num[0] == '0':
#   raise ValueError
# res = ''
# for i in range(len(num) - 1, -1, -1):
#   j = len(res) - 1
#   while j >= 0:
#     if res[j] == num[i]:
#       break
#     j -= 1
#   if j < 0:  # no duplication, pre-append the current element
#     res = res + num[i]
# print(res)

# line = 'asdfasd\n'
# l = set(line.strip())
# print(l)
# print(len(set(l)))
# print(line.strip()[::-1])

import sys

# line = list(map(int, sys.stdin.readline().strip().split(' ')))
# N, m = line[0], line[1]
# v = [0] * m
# p = [0] * m
# q = [0] * m
# an = [[] for _ in range(m)]
#
# for i in range(m):
#   line = list(map(int, sys.stdin.readline().strip().split(' ')))
#   v[i], p[i], q[i] = line[0], line[1], line[2]
#
# for i in range(m):
#   if q[i] != 0:
#     an[q[i] - 1].append(i)
# print(v, p, q, an)
#
# res = [[0] * (N + 1) for i in range(m + 1)]
# for i in range(1, m + 1):
#   for j in range(N, 0, -10):
#     if q[i - 1] == 0:
#       if v[i - 1] <= j:  # main item
#         res[i][j] = max(res[i - 1][j], res[i - 1][j - v[i - 1]] + p[i - 1] * v[i - 1])  # max(donot buy, buy item i,)
#       else:
#         res[i][j] = res[i - 1][j]
#     else: # current item is accessory
#       if i == an[q[i - 1]-1][0]: # it's the first accessory of the main item
#         if v[q[i - 1] - 1] + v[i - 1] <= j:
#           res[i][j] = max(res[i - 1][j],
#                         res[i - 1][j - v[i - 1] - v[q[i - 1] - 1]] + v[i - 1] * p[i - 1] + p[q[i - 1] - 1] * v[q[i - 1] - 1])
#         else:
#           res[i][j] = res[i-1][j]
#       elif i == an[q[i - 1]-1][1]: # it's the second accessory of the main item
#         imain = q[i - 1] - 1  #index of main item: q[i - 1] - 1
#         ifa = an[q[i - 1] - 1][0]-1  #the index of first accessory: an[q[i - 1] - 1][0]-1
#         if v[imain] + v[i - 1] <= j < v[imain] + v[i - 1] + v[ifa]:
#           res[i][j] = max(res[i - 1][j],
#                           res[i - 1][j - v[imain] - v[i - 1]] + p[imain] * v[imain] + v[i - 1] * p[i - 1])
#         elif v[imain] + v[i - 1] + v[ifa] <= j:
#           res[i][j] = max(res[i - 1][j],
#                          res[i - 1][j - v[imain] - v[i - 1] - v[ifa]]
#                         + v[imain] * p[imain]) \
#                         + v[i - 1] * p[i - 1] \
#                         + v[ifa] * p[ifa]
#   # print(res[1])
# print(res[m][int(N // 10) * 10])




# money, things = map(int, input().split())
# money = money // 10  # money都是10的整数，整除后，减小循环次数
# # 三列分别表示主件，附件1，附件2
# weight = [[0] * 3 for _ in range(0, things + 1)]  # 价格
# value = [[0] * 3 for _ in range(0, things + 1)]  # 价值=价格*重要度
# result = [[0] * (money + 1) for _ in range(things + 1)]
# for i in range(1, things + 1):
#   prices, degree, depend = map(int, input().split())  # 分别为价格，重要性，主附件
#   prices = prices // 10
#
#   if depend == 0:  # 主件
#     weight[i][0] = prices
#     value[i][0] = prices * degree
#
#   elif weight[depend][1] == 0:  # 附件
#     weight[depend][1] = prices  # 第一个附件
#     value[depend][1] = prices * degree
#
#   else:
#     weight[depend][2] = prices  # 第二个附件
#     value[depend][2] = prices * degree
#
# # 遍历计算
# for i in range(1, things + 1):
#   for j in range(money, 9, -10):
#     if j >= weight[i][0]:  # 可以容下第i个主件时,比较不放第i个或者放第i个物品的价值
#       result[i][j] = max(result[i - 1][i], result[i - 1][j - weight[i][0]] + value[i][0])
#     else:
#       result[i][j] = result[i - 1][j]
#     if j >= (weight[i][0] + weight[i][1]):  # 可以容下第i个主件和此主件的第1个附件时
#       result[i][j] = max(result[i - 1][j], result[i - 1][j - weight[i][0] - weight[i][1]] + value[i][0] + value[i][1])
#     else:
#       result[i][j] = result[i - 1][j]
#     if j >= (weight[i][0] + weight[i][2]):  # 可以容下第i个主件和此主件的第2个附件时
#       result[i][j] = max(result[i - 1][j],
#                          result[i - 1][j - weight[i][0] - weight[i][2]] + value[i][0] + value[i][2])
#     else:
#       result[i][j] = result[i - 1][j]
#     if j >= (weight[i][0] + weight[i][1] + weight[i][2]):  # 可以容下第i个主件和此主件的第1个附件和第2个附件时
#       result[i][j] = max(result[i - 1][j],
#                          result[i - 1][j - weight[i][0] - weight[i][1] - weight[i][2]] + value[i][0] + value[i][1] +
#                          value[i][2])
#     else:
#       result[i][j] = result[i - 1][j]
# print(result[things][money] * 10)


# def left_max(heights):
#   num = len(heights)
#   res = [1 for _ in range(num)]
#   for i in range(num):
#     for j in range(i):
#       if heights[i] > heights[j] and res[i] < res[j] + 1:
#         res[i] = res[j] + 1
#   return res
#
# while True:
#   try:
#     N = int(input())
#     heights = list(map(int, input().split()))
#     left_res = left_max(heights)
#     right_res = left_max(heights[::-1])[::-1]
#     sum_res = []
#     for i in range(N):
#       sum_res.append(left_res[i] + right_res[i])
#     print(N - max(sum_res) + 1)
#   except:
#     break
#
# while True:
#   try:
#     m, n = list(map(int, input().split()))
#     res = [[0 for _ in range(n)] for _ in range(m)]
#     for i in range(m):
#       res[i][0] = 1
#     for j in range(n):
#       res[0][j] = 1
#     for i in range(1, m):
#       for j in range(1, n):
#         if i == j:
#           res[i][j] = res[i][j - 1] + res[i - j][j]
#         elif i > j:
#           res[i][j] = res[i][j-1] + res[i-j-1][j]
#         else:
#           res[i][j] = res[i][j-1]
#     print(res[m-1][n-1])
#   except:
#     break
#
# class Linked_Node:
#   def __init__(self, value):
#     self.value = value
#     self.next = None
#
#
# class Single_linked_list:
#   def __init__(self):
#     self.head = None
#     self.tail = None
#     self.length = 0
#
#   def add_node(self, new_node):
#     if not isinstance(new_node, Linked_Node):
#       new_node = Linked_Node(new_node)
#
#     if self.head is None:
#       self.head = new_node
#     else:
#       self.tail.next = new_node
#     self.tail = new_node
#     self.length += 1
#
#   def get_kth_to_tail(self, k):
#     current = self.head
#     i = 1
#     while current.next is not None and i + k <= self.length:
#       current = current.next
#       i += 1
#     return current.value
#
# while True:
#   try:
#     single_linked_list \
#       = Single_linked_list()
#     n = int(input())
#     l = list(map(int, input().split()))
#     for i in range(n):
#       single_linked_list.add_node(l[i])
#     k = int(input())
#     if k == 0:
#       print(0)
#     res = single_linked_list.get_kth_to_tail(k)
#     print(res)
#   except:
#     break


# while True:
#   try:
#     line = list(map(int, input().split()))
#     n, m = line[0], line[1]
#     matrix = []
#     for i in range(n):
#       matrix.append(list(input()))
#     print(matrix)
#
#   except:
#     break


n = 5
capacity = 10
weights = [2, 2, 6, 5, 4]
values = [6, 3, 5, 4, 6]

dp = [[0 for i in range(capacity+1)] for j in range(n+1)]
for i in range(1, n+1):
  for j in range(1, capacity+1):
    dp[i][j] = dp[i - 1][j]
    if j >= weights[i - 1] and dp[i][j] < dp[i - 1][j - weights[i - 1]] + values[i - 1]:
      dp[i][j] = dp[i - 1][j - weights[i - 1]] + values[i - 1]

print(dp[-1][-1])
