"""
1. Start with our empty res list
2. Then we lock one pointer in the for loop and the otehr two pointers are free tomvoe depending on the condiiton.
3. Edge cases:
    - 
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                threesum = a + nums[l] + nums[r]

                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
