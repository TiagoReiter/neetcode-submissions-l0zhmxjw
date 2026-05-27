"""
1. Start with a prevmap, init as empty list.
2. Add our pre courses to the list, Structure: [crs, pre]
3. Set up our dfs, loop through and check. 
    1. 
4. Base cases are: First empty list, return True there and also visiting

1: [0,2]
2: [0,1] and so on
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevm = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites: 
            prevm[crs].append(pre)
        
        visiting = set()
        
        def dfs(crs):
            if crs in visiting:
                return False
            if prevm[crs] == []:
                return True
            
            visiting.add(crs)
            for pre in prevm[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            prevm[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
