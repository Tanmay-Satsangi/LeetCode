class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        n = len(arr)
        i = 1

        while(True):
            if i not in arr:
                count += 1
                if count == k:
                    return i
            i += 1

        # return (i - 1)
        
