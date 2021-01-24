from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    res = list()
    for l in zip(*strs):
      if len(set(l)) == 1:  # exactly the same letter
        res.append(l[0])
      else:
        break
    return "".join(res)
