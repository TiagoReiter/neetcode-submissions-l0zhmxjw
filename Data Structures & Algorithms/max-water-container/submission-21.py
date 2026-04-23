"""
Interested in the max area. Max area is defined but the maximum width and 
the min height between two different bars: 
[x x x x x x x]
 0 1 2 3 4 5 6
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                res = max(res, min(heights[i],heights[j]) * (j - i))
        
        return res
             
        