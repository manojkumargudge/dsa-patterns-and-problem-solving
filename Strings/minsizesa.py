''' Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.'''

class Solution:
    def minSubArrayLen(self, target,nums):
        
        left = 0
        current_sum = 0
        minimum = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]
        
            while current_sum>= target:
                minimum = min(minimum,right-left+1)

                current_sum -= nums[left]
                left +=1

        return 0 if minimum == float("inf") else minimum  

nums = [2,3,1,2,4,3]
target = 7
sol = Solution()
print(sol.minSubArrayLen(target,nums))
