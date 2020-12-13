
class Solution:
  """
  Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
  Follow up: Could you solve it without converting the integer to a string?
  """

  def isPalindrome(self, x: int) -> bool:
    # converting the integer to a string
    #         s = str(x)
    #         i = 0
    #         j = len(s)

    #         while i < j:
    #             if s[i] == s[j-1]:
    #                 i += 1
    #                 j -= 1
    #             else:
    #                 return False
    #         return True

    # do not converting the integer to a string
    if x < 0:
      return False
    else:
      # detemin the length of the loop
      div = 1
      i = 0
      while div != 0:
        div = x // (10 ** i)
        i += 1
      i -= 1
      j = 1
      while j <= i // 2:
        if (x // 10 ** (j - 1)) % 10 != x // 10 ** (i - j) % 10:
          return False
        j += 1
      return True


sol = Solution()
print(sol.isPalindrome(121))