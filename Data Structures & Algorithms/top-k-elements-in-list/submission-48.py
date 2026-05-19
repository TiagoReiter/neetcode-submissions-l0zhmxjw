"""
 [ 1 2 3 3 3 4 2 4]
 1. Count by appearance with help of ahsh table.
 2. Covnert to list and sort.
 3. take the most frequent elements and reutrn
 counts[3] = 3
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count  = {}
        res = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        temp = []
        for num, cnt in count.items():
            temp.append([cnt, num])

        temp.sort()

        while len(res) < k:
            res.append(temp.pop()[1])
        return res


    