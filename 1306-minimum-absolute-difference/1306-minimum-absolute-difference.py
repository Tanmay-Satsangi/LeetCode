class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_diff = float('inf')
        n = len(arr)
        curr = []

        for i in range(n - 1):
            diff = (arr[i + 1] - arr[i])
            
            if (diff == min_diff):
                curr.append([arr[i], arr[i + 1]])
            elif (diff < min_diff):
                curr = []
                curr.append([arr[i], arr[i + 1]])
                min_diff = diff

        return curr
        