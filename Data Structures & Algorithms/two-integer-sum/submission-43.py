class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        diff = target - val
        Interested in index not values
        - So if current nums[i] + diff[val] == target return
        1. Init counter
        2. If nums[i] + diff[val] == target:
                return 

        """
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

        return []