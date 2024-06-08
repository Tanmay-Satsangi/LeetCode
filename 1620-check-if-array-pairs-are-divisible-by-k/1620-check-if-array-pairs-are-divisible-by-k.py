class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        nums = [0] * k
        n = len(arr)

        #Modulo array
        for i in range(n):
            rem = (arr[i] % k + k) % k
            nums[rem] += 1

        #odd count at 0th index
        if (nums[0] % 2 != 0):
            return False

        for i in range(1, (k // 2) + 1):
            if nums[i] != nums[k - i]:
                return False

        return True