import collections


class Solution:
  """
  Given a chemical formula (given as a string), return the count of each atom.
  """

  def countOfAtoms(self, formula: str) -> str:
    """
    my first impression is that it can be soloved by using recursion;
    the difficult part is to handle the parenthesis, when do we need to handle it?
    -> when it encounters the right parenthesis, we need to multiply the previous
    formula, i.e. the characters after the left parenthesis. So we need a counter
    count the characters after the left parenthesis.
    """
    N = len(formula)
    self.i = 0

    def detect_sub_formula():
      counter = collections.Counter()

      while self.i < N and formula[self.i] != ')':
        if formula[self.i] == '(':
          self.i += 1
          for atom, c in detect_sub_formula().items():
            counter[atom] += c
        else:
          # detect atom name
          s = self.i
          self.i += 1
          while self.i < N and formula[self.i].islower():
            self.i += 1
          atom = formula[s:self.i]
          # detect atom amount
          s = self.i
          while self.i < N and formula[self.i].isdigit():
            self.i += 1
          if self.i > s:
            counter[atom] += int(formula[s:self.i])
          else:
            counter[atom] += 1

      # encouter the right parentheis, detect formula amount
      self.i += 1
      s = self.i
      while self.i < N and formula[self.i].isdigit():
        self.i += 1
      if s < self.i:
        m = int(formula[s:self.i])
        for atom in counter:
          counter[atom] *= m
      return counter

    res = []
    c = detect_sub_formula()
    for atom in sorted(c):
      res.append(atom)
      if c[atom] > 1:
        res.append(str(c[atom]))
    res = "".join(res)
    return res


sol = Solution()
print(sol.countOfAtoms("H2O"))
