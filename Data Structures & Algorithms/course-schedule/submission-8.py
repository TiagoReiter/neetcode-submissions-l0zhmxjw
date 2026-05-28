"""
1. Create a map which shows which course we have to take before going onto other course
2. WE have to detect cyclces, otherwise we end up in a never ending loop 
3. We can explore each parent node and its kids by a recursive dfs
    1 : [2, 4]
    2 : [2, 3]
    .... 
    v
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