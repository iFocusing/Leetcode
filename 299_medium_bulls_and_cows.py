class Solution:
  # def getHint(self, secret: str, guess: str) -> str:
  #   lg = len(guess)
  #   ls = len(secret)
  #   bulls = 0
  #   cows = 0
  #   tmp = secret
  #   for i in range(lg-1, -1, -1):
  #     if guess[i] == secret[ls-1-(lg-1-i)]:
  #       bulls += 1
  #       tmp = tmp[0:ls - 1 - (lg - 1 - i)] + '*' + tmp[ls - 1 - (lg - 1 - i) + 1:]
  #     else:
  #       for j in range(ls - 1, -1, -1):
  #         if guess[i] == tmp[j] and guess[lg-1-(ls-1-j)] != tmp[j]:
  #           cows += 1
  #           tmp = tmp[0:j] + '*' + tmp[j + 1:]
  #           break
  #   return str(bulls) + 'A' + str(cows) + 'B'  # complexity O(n^2)


  def getHint(self, secret: str, guess: str) -> str:
    lg, ls = len(guess), len(secret)
    g_dict, s_dict= dict(), dict()
    bulls, cows = 0, 0

    for i in range(lg-1, -1, -1):
      if guess[i] == secret[ls-1-(lg-1-i)]:
        bulls += 1
      else:
        if guess[i] in g_dict:
          g_dict[guess[i]] += 1
        else:
          g_dict[guess[i]] = 1
        if secret[ls-1-(lg-1-i)] in s_dict:
          s_dict[secret[ls-1-(lg-1-i)]] += 1
        else:
          s_dict[secret[ls-1-(lg-1-i)]] = 1
    for k in g_dict:
      if k in s_dict:
        cows += min(g_dict[k], s_dict[k])
    return str(bulls) + 'A' + str(cows) + 'B'  # complexity O(n)

sol = Solution()
print(sol.getHint('1123', '0111'))