''' You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 '''

class Solution:
    def charecter_replacement(self,s,k):
        left = 0
        count = {}
        max_count = 0
        answer = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
            max_count = max(max_count,count[s[right]])

            while (right-left+1) - max_count>k:
                count[s[left]]-=1
                left+=1

            answer = max(answer,right-left+1)

        return answer

s = "ABAB"
k = 2
sol = Solution()
print(sol.charecter_replacement(s,k))
