"""
k most frequent elements:
    1. count elements num as index count as val
    2. convert to list
    3. sort
    4. pop
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        temp = []
        for val, cnt in count.items():
            temp.append([cnt, val])
        
        temp.sort()

        while len(res) < k:
            res.append(temp.pop()[1])
        return res