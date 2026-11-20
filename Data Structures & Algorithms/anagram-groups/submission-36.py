class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. Init default dict
        2. Sort string and join
        3. add sorted 
        """

        res = defaultdict(list)

        for s in strs:
            sorteds = "".join(sorted(s))
            res[sorteds].append(s)
        
        return list(res.values())