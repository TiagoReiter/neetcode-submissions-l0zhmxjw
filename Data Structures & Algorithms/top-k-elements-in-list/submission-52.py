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
        
        count  = {}
        res = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        for num, cnt in count.items():
            heapq.heappush(heap, (cnt, num))

            if len(heap) > k:
                heapq.heappop(heap)
        return [num for cnt, num in heap]