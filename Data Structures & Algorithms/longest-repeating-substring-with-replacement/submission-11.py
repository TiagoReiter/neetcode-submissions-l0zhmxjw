"""
1. Count the actual number of appearance
2. The best to replace with teh most frequent chracter -> less replacements
3. [A A A B A B B]
    A: 4
    5: 3
    window_size - max_count <= k
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = l = 0
        maxc = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxc = max(maxc, count[s[r]])
            if (r-l+1) -maxc > k:
                count[s[l]] -= 1
                l+=1
            res = max(res, r-l +1)
        return res