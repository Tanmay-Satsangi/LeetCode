# https://www.youtube.com/watch?v=PqEiJDdt3S4
# TC = O(N2)
# SC = O(1)

#Property of Traingle: Sum of any two sides should be strictly greater then the third side
# i.e (a + b) > c
    

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)

        nums.sort()        
        count = 0

        for i in range(n - 1, 1, -1):
            l = 0
            r = i - 1

            while (l < r):
                if (nums[l] + nums[r] > nums[i]): #Here three sides of triangle are arr[l], arr[r] and arr[i]
                    # (if arr[l] + arr[r] > arr[i] then definitely upcoming greater values of arr[l] is always greater because array is sorted)
                    count += (r - l)
                    r -= 1
                else:
                    # If sum of arr[l] + arr[r] is smaller then arr[i] then we have to increase the value 
                    l += 1

        return count

        