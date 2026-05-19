class Solution:
    def findMin(self, nums: List[int]) -> int:
        minv = nums[0]
        for n in nums:
            minv = min(minv, n)
        return minv