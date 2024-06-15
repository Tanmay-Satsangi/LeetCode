# https://www.youtube.com/watch?v=UUjeqglXaSQ
# lee215 Solution from discuss section

# Intuition:
# Before we do it in 2D plane, let's try it in 1D.
# Given 2 segment (left1, right1), (left2, right2), how can we check whether they overlap?
# If these two intervals overlap, it should exist an number x,

# left1 < x < right1 && left2 < x < right2

# left1 < x < right2 && left2 < x < right1

# left1 < right2 && left2 < right1

# This is the sufficient and necessary condition for two segments overlap.

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return (
            rec1[0] < rec2[2] and
            rec1[1] < rec2[3] and
            rec1[2] > rec2[0] and
            rec1[3] > rec2[1]
        )