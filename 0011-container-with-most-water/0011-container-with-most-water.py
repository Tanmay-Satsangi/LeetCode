# https://www.youtube.com/watch?v=Cm_cdYiR6e8
# TC = O(N)
# SC = O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        curr_water = 0
        max_water = 0

        n = len(height)
        l = 0
        r = n - 1

        while (l < r):
            #Area of rectangle: length * breadth
            curr_water = min(height[l], height[r]) * (r - l)
            max_water = max(max_water, curr_water)

            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1

        return max_water

        