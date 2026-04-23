"""
STEPS:
[-2 -1 3 2 -2 0]
[-2 -1 -1 0 3 4] <- skip -2 EC2
  i  l        r
[1 2 3 4 5 6] <- not valid EC1
 
1. Init empty list and sort
2. Lock one of the three values in a for list
    1. EC1: If first value already over 0 we can break
    2. EC2: If a value repeats we just skip the value
3. Init two pointers starting at i+1 and len(nums) -1
3.1 Init our three sum and from that construct hte fi statements
4. For the left pointer we have to apply EC2.
5. append to res and and adjust pointers 
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

            l, r = i+1, len(nums) - 1

            while l < r:
                threesum = a + nums[l] + nums[r]

                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return res
                
