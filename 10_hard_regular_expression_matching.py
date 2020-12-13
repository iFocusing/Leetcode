

class Solution:
  """
  Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:

  '.' Matches any single character.​​​​
  '*' Matches zero or more of the preceding element.
  The matching should cover the entire input string (not partial).

  """
  def isMatch(self, s: str, p: str) -> bool:
    # recursion
    # if not p: return not s # if a string is empty string, i.e. '', then bool(p) is false
    # if len(p) >= 2 and p[1] == '*':
    # return self.isMatch(s, p[2:]) or ((bool(s) and (p[0] == '.' or s[0] == p[0])) and  self.isMatch(s[1:], p))
    # else:
    #     return (bool(s) and (p[0] == '.' or s[0] == p[0])) and self.isMatch(s[1:], p[1:])

    # some calls in the recursion can be cached
    self.s, self.p, self.cache = s, p, {}
    return self.matching(0, 0)

  def matching(self, i, j):
    if (i, j) not in self.cache:
      if j == len(self.p):
        res = i == len(self.s)
      else:
        if j + 1 < len(self.p) and self.p[j + 1] == '*':
          res = self.matching(i, j + 2) or (
                (bool(self.s[i:]) and (self.p[j] == '.' or self.s[i] == self.p[j])) and self.matching(i + 1, j))
        else:
          res = (bool(self.s[i:]) and (self.p[j] == '.' or self.s[i] == self.p[j])) and self.matching(i + 1, j + 1)
      self.cache[(i, j)] = res
    return self.cache[i, j]


sol = Solution()
print(sol.isMatch("aab", "c*a*b"))