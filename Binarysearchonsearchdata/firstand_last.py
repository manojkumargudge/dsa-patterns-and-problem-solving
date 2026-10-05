'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.'''

'''Find
First occurrence of target
Last occurrence of target'''

class Solution:
    def search_range(self,nums,target):

        def first_find():
            left = 0 
            right = len(nums)-1
            ans =-1


            while left <= right:
                mid = (left+right)//2

                if nums[mid]== target:
                    ans = mid
                    right = mid-1
                elif nums[mid]<target:
                    left = mid+1
                else:
                    right = mid - 1
            return ans

        def second_find():
            left = 0 
            right = len(nums)-1
            ans =-1

            while left<=right:
                mid= (left + right)//2
                if nums[mid]==target:
                    ans = mid
                    left = mid+1
                elif nums[mid]<target:
                    left = mid+1
                else:
                    right = mid -1
            return ans


        return [first_find(),second_find()]

nums = [5,7,7,8,8,10] 
target = 8
sol = Solution()
print(sol.search_range(nums,target))



