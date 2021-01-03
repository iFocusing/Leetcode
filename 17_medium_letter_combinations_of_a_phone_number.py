from typing import List


class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    dls = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    if len(digits) == 0: return []

    # simple iterative
    # res = ['']
    # for d in digits:
    #     tmp = []
    #     for item in res:
    #         for l in dls[d]:
    #             tmp.append(item + l)
    #     res = tmp
    # return res

    # recursion
    res = []

    def fun(pre, nxt):
      if len(nxt) == 0:
        res.append(pre)
      else:
        for l in dls[nxt[0]]:
          fun(pre + l, nxt[1:])

    fun("", digits)
    return res


sol = Solution()
print(sol.letterCombinations('23'))