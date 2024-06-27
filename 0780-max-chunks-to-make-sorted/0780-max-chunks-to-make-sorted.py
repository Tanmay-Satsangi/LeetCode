# https://www.youtube.com/watch?v=XZueXHOhO5E

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxm = 0
        chunks_count = 0
        n = len(arr)

        for i in range(n):
            maxm = max(maxm, arr[i])

            if maxm == i:
                chunks_count += 1

        return chunks_count