class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(i,total,path):
            if total == target:
                res.append(path[:])
                return
            
            if i >= len(candidates) or total > target:
                return
            
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                backtrack(j,total+candidates[j],path)
                path.pop()
            
        backtrack(0,0,[])

        return res
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         ans = []
#         ds = []
#         self.findcombination(0, target, candidates, ans, ds)
#         return ans
    
#     def findcombination(self, index: int, target: int, candidates: List[int], ans, ds):
#         if(index >= len(candidates)):
#             if(target == 0):
#                 ans.append(ds[:])
#             return
        
#         if(candidates[index] <= target):
#             ds.append(candidates[index])
#             self.findcombination(index, target - candidates[index], candidates, ans, ds)
#             ds.pop()

#         self.findcombination(index + 1, target, candidates, ans, ds)