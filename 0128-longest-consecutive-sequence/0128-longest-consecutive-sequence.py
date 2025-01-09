# The time complexity to search for an element in a set is generally O(1). However, in rare cases of hash collisions, it may take O(n) time. Despite this, the we can say that the time complexity is O(1).

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr_num = 0
        curr_streak = 0
        max_streak = 0
        nums_set = set(nums)

        for num in nums_set:
            if (num - 1) not in nums_set:
                curr_num = num
                curr_streak = 1

                while (curr_num + 1) in nums_set:
                    curr_num += 1
                    curr_streak += 1

                max_streak = max(max_streak, curr_streak)

        return max_streak

