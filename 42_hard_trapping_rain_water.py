from typing import List


class Solution:
  def trap(self, height: List[int]) -> int:
    water, t = 0, 0
    for i, h in enumerate(height[:-1]):
      if h >= t:
        t = min(h, max(height[i + 1:]))
      else:
        water += t - h
    return water
