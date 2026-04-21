"""
- Use default dict -> can be initlized with a list
- Gonna use the sorted(s) of strs as the key
- Add each inidvidual unsorted key to the list
- Print out the values of the dict.
- 
map = defauldict[]
    for string ins strs:
        add string at sorted_ string
    
    return [map.values()]
    "b c a" -> "a" "b""c" -> abc 
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count = defaultdict(list)
        res = []
        for s in strs:
            sorted_s = "".join(sorted(s))
            count[sorted_s].append(s)
        
        return list(count.values())