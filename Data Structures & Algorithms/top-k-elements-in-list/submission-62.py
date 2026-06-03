"""
 [ 1 2 3 3 3 4 2 4]
 1. Count by appearance with help of ahsh table.
 2. Covnert to list and sort.
 3. take the most frequent elements and reutrn
 counts[3] = 3
"""
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        heap = []

        for num, cnt in count.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res