"""
first for easier look up we
1. need to count our appearance
2. one popinte rone the left side and one pointer in teh for loop. and 
what we check is if windowsie - maxc < k -> we can replace
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = res = 0
        maxc = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxc = max(maxc, count[s[r]])

            if (r - l + 1) - maxc > k:
                count[s[l]] -= 1
                l += 1
            res = max((r - l + 1 ), res)
        
        return res