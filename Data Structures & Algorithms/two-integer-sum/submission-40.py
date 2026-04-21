"""
find index so that nums[i] + nums[j] = target
nums[j] = target - nums[i]
IDEA:
- Use a dict where we save {number:index}
- Check if the difference is in dict
    -> If yes return i , j 
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in seen:
                return  [seen[diff], i]
            seen[n] = i
        