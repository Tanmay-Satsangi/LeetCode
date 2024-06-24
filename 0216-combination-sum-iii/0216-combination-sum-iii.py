class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.backtrack(1, [], res, k, n)
        return res

    def backtrack(self, start, curr, res, k, target):
        if target == 0 and len(curr) == k:
            res = res.append(list(curr))
            return res

        if len(curr) > k:
            return

        for i in range(start, 10):
            curr.append(i)
            self.backtrack(i + 1, curr, res, k, target - i)
            curr.pop()
