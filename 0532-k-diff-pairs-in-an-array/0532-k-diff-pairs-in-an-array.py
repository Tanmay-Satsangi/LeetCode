# https://www.youtube.com/watch?v=a2dCHUM6Mq4
# TC = O(N)
# SC = O(N)

# arr[j] - arr[i] == k
# => arr[j] = k + arr[i]

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        visited_count = {}
        n = len(nums)
        count = 0

        for num in nums:
            if num not in visited_count:
                visited_count[num] = 1
            else:
                visited_count[num] += 1 

        #We have to find the k such that arr[j] - arr[i] = k
        #So, we can write this statement in something like that arr[j] = k + arr[i]

        #iterate key of "visited_count" dictionary to avoid duplicates
        
        for key in visited_count:
            if (k > 0 and (key + k) in visited_count) or (k == 0 and visited_count[key] > 1): #visited_count[k] > 1 To form pairs to himself because k is 0.
                count += 1
        return count

            

        