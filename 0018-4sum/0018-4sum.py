class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        if n < 4:
            return []

        nums.sort()
        i = 0
        ans = []

        while (i < n):
            j = i + 1

            while (j < n):
                left = j + 1
                right = n - 1

                while left < right:
                    sums = nums[i] + nums[j] + nums[left] + nums[right]
                    if sums == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while (left < n and nums[left] == nums[left - 1]):
                            left += 1

                        while (right >= 0 and nums[right] == nums[right + 1]):
                            right -= 1

                    elif sums < target:
                        left += 1
                    else:
                        right -= 1

                j += 1
                while (j < n and nums[j] == nums[j - 1]):
                    j += 1

            i += 1
            while (i < n and nums[i] == nums[i - 1]):
                i += 1

        return ans
