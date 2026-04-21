"""
TOp most frequent elements:
1. Count the number of appearance with help of dict and get fucntion
2. COnvert to a list with (cnt, val)
3. sort
4. return the last k elements
---
[1 2 3 3 3], k =2
count = 1:1, 2:1 , 3:3
tmp = 1,1 1,2 3,3 

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        tmp = []

        for val, cnt in count.items():
            tmp.append([cnt, val])
        tmp.sort()

        while k > 0:
            res.append(tmp.pop()[1])
            k -= 1
        return res
