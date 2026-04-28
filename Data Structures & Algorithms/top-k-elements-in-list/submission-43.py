"""
TOp most frequent elements:
1. Count the number of appearance with help of dict and get fucntion
. COnver 
[1 2 3 3 3], k =2
count = 1:1, 2:1 , 3:3
tmp = 1,1 1,2 3,3 

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        heap = 0
        res = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        heap = []

        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res