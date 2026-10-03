'''Given a string s, find the length of the longest substring without duplicate characters.'''


class Solution:
    def longest_substring(self,s):
        maxi = 0
        n = len(s)


        for i in range(len(s)):
            my_set = set()
            for j in range(i+1,n):
                if s[j] in my_set:
                    break
                maxi = max(maxi,j-i+1)
                my_set.add(s[j])

        return maxi

s = "abcabcbb"
sol = Solution()
print(sol.longest_substring(s))
