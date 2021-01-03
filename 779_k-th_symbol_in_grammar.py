class Solution:
  def kthGrammar(self, N: int, K: int) -> int:
    if N == 1 and K == 1: return 0
    # iterative - time limit exceeded
    # res = [0]
    # while N - 1 > 0:
    #     tmp = list()
    #     for i in res:
    #         if res[i] == 0:
    #             tmp.append(0)
    #             tmp.append(1)
    #         else:
    #             tmp.append(1)
    #             tmp.append(0)
    #     res = tmp
    #     N -= 1
    # return res[K-1]

    # recursion
    m = 2 ** (N - 1) // 2
    if m >= K:
      return self.kthGrammar(N - 1, K)
    else:
      r = self.kthGrammar(N - 1, (K + 1) // 2)
      if r == 0:
        if K % 2 == 0:
          return 1
        else:
          return 0
      else:
        if K % 2 == 0:
          return 0
        else:
          return 1


sol = Solution()
print(sol.kthGrammar(30, 112323))