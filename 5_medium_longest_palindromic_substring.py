
class Solution:
  def longestPalindrome(self, s: str) -> str:
    length = len(s)
    if length == 1:
      return s
    elif length == 2:
      if s[0] != s[1]:
        return s[0]
      else:
        return s
    result = ''
    for i in range(0, len(s)):
      longest_length_1 = self.find_palindrome(s, i, i)  # find a odd palindrome
      longest_length_2 = self.find_palindrome(s, i, i + 1)  # find a even palindrome
      if longest_length_1 > longest_length_2:
        longestPalindrome = s[i - longest_length_1 // 2: i + longest_length_1 // 2 + 1]
      else:
        longestPalindrome = s[i + 1 - longest_length_2 // 2: i + longest_length_2 // 2 + 1]
      if len(longestPalindrome) > len(result):
        result = longestPalindrome
    return result

  def find_palindrome(self, s: str, left: int, right: int) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1
    return right - left - 1


sol = Solution()
print(sol.longestPalindrome("babad"))