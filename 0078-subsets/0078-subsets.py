# RECURSIVE APPROACH - DFS(Depth first search)

# TC = O(N * (2 ^ N))
# SC = O(N) If we ignore the output space complexity i.e. res.
# SC = O(N * (2 ^ N)) If consider the output space complexity 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(0, [], nums, res)
        return res

    def backtrack(self, start, curr, nums, res):
        res.append(list(curr))

        for i in range(start, len(nums)):
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums, res)
            curr.pop()