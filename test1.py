# while True:
#   try:
#     tlv = input().split()
#     t = int(''.join(tlv[0:2]), 16)
#     l = int(''.join(tlv[2:6]), 16)
#     v = tlv[6:-1]
#     last = tlv[-1]
#     content = ''
#     if len(v) != l:
#       content = 'LEN_ERR'
#     elif len(v) == 0:
#       content = ""
#     else:
#       pass
#     print('{' + 'T:' + str(t) + ',L:' + str(l) + ',V:' + content + '}')
#   except:
#     break

# def dfs(mat, i, j, count):
#   if mat[i][j] == -1:
#     return 0
#   if mat[i][j] == 1:
#     count += 1
#   if i == len(mat) - 1 and j == len(mat) - 1:
#     return count
#   if i != len(mat) - 1 or j != len(mat) - 1:
#     print(i, j)
#     right = dfs(mat, i, j + 1, count) # right
#     down = dfs(mat, i + 1, j, count) # down
#     print(right, down)
#     return max(right, down)


def dp(mat):
  n = len(mat)
  direction = [(0, 0)]
  res = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(1, n):
    if mat[0][i] == 1:
      res[0][i] = res[0][i-1] + 1
    elif mat[0][i] == 0:
      res[0][i] = res[0][i - 1]
    else:
      res[0][i] = -100

  for j in range(1, n):
    if mat[j][0] == 1:
      res[j][0] = res[j-1][0] + 1
    elif mat[j][0] == 0:
      res[j][0] = res[j-1][0]
    else:
      res[j][0] = -100

  for i in range(1, n):
    for j in range(1, n):
      if mat[i][j] != -1:
        if res[i][j-1] + mat[i][j] >= res[i-1][j] + mat[i][j]:
          res[i][j] = res[i][j-1] + mat[i][j]
          direction.append((i, j - 1))
        else:
          res[i][j] = res[i-1][j] + mat[i][j]
          direction.append((i-1, j))
      else:
        res[i][j] = -100
  direction.append((n-1, n-1))
  # print(direction)
  return res[n-1][n-1], direction

while True:
  try:
    n = int(input())
    mat = list()
    for i in range(n):
      l = list(map(int, input().split()))
      mat.append(l)

    num1, direction = dp(mat)
    for item in direction[::-1]:
      if mat[item[0]][item[1]] == 1:
        mat[item[0]][item[1]] = 0
    num2, _ = dp(mat)
    num = num1 + num2
    print(num)
  except:
    break
