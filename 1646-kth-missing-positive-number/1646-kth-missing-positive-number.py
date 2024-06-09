class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        n = len(arr)
        i = 1

        while(count != k):
            if i not in arr:
                count += 1
            i += 1

        return (i - 1)
        
