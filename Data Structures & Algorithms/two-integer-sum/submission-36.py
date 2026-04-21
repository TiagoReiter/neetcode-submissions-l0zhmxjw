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
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] + nums[i] == target:
                    return [i,j ]