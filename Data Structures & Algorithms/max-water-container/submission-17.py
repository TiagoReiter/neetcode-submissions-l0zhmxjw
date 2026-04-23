"""
Interested in the max area. Max area is defined but the maximum width and 
the min height between two different bars: 
[x x x x x x x]
 0 1 2 3 4 5 6
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1

        while l < r:
            A = (r - l) * min(heights[l], heights[r])
            res = max(A,res)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
        return res

             
        