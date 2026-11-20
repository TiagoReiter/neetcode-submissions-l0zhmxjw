class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dict = count of numbers. keys numbers and count is value
        #sort -> convert to list
        #take k last elements which are the largest count
        cnt = defaultdict(list)

        for i in range(len(nums)):
            cnt[nums[i]] = 1 + cnt.get(nums[i], 0)
        
        heap = []
        for num in cnt.keys():
            heapq.heappush(heap, [cnt[num], num])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res