"""
Longest substring without repeating. 
IDEA:
Init set. Add to set as long as possible. Update substring max  length and pointers.
x y z 

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l +1)
        return res