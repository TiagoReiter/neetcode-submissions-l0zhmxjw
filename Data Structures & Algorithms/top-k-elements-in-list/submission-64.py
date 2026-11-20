class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        cnt.item = (val, cnt)
        """
        res = []
        cnt = {}
        for i in range(len(nums)):
            cnt[nums[i]] = 1 + cnt.get(nums[i], 0)
        
        temp  = []
        for val, cnt in cnt.items():
            temp.append([cnt, val])
        
        temp.sort() 

        while len(res) < k:
            res.append(temp.pop()[1])
        
        return res
