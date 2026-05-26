class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt = {}

        for num in nums:
            cnt[num] = 1 + cnt.get(num, 0)
        
        heap = []
        
        for num, freq in cnt.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res