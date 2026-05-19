"""
1. Container with msot water. 
2. constrained by the shorter height
3. Two pointer -> a  = (r - l) * min(l, r)
4. Need to save the largest a and update our l r depending on its size
    meaning we save max(a, res)
5. so if l < r: l+ and if r < l: r- while l < r:
6. [ 1 7 3 5 4 9 8 3 2  1] 
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            a = min(heights[l], heights[r]) * (r - l)
            res = max(res, a)
            if heights[l] <= heights[r]:
                l += 1
            
            else:
                r -= 1
        return res
        
