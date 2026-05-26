class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt = {}

        for num in nums:
            cnt[num] = 1 + cnt.get(num, 0)
        
        temp = []
        for num, freq in cnt.items():
            temp.append([freq, num])
        
        temp.sort()
        res = []
        while len(res) < k:
            res.append(temp.pop()[1])
        return res