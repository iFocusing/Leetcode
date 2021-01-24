import numpy as np


def clustering(data, k):
  N, m = data.shape
  S = {np.random.randint(0, N): data[np.random.randint(0, N)]}
  for i in range(1, k):
    index = find_centroid(S, data)
    S[index] = data[index]

  flag = False
  data_cluster = []
  while not flag:
    data_cluster = []
    for i in range(N):
      if i in S.keys():
        data_cluster.append(list(S.keys()).index(i))
      else:
        l = []
        for j in range(k):
          l.append(calc_distance(S[list(S.keys())[j]], data[i]))
        data_cluster.append(l.index(min(l)))
    centroid_sum = [[] for _ in range(k)]
    for i in range(N):
      centroid_sum[data_cluster[i]].append(data[i])
    S, flag = update_S(S, centroid_sum)
  return data_cluster # N * 1 的一维向量


def update_S(S, centroid_sum):
  S_res = {}
  flag = True
  for i, value in S.items():
    S_res[i] = np.mean(centroid_sum[list(S.keys()).index(i)])
    if not (S[i] == S_res[i]).all():
      flag = False
  return S_res, flag


def find_centroid(S, data):
  N, m = data.shape
  res_index, res_distance = 0, 0
  for i in range(N):
    if i not in S.keys():
      distance = calc_distance(S[list(S.keys())[0]], data[i])
      if distance > res_distance:
        res_distance = distance
        res_index = i
  return res_index

def calc_distance(v1, v2):
  res = np.sqrt(np.sum(np.square(v1-v2)))
  return res


data = np.array([[1,2],[2,3],[5,6],[1,2]])
print(clustering(data, 2))
