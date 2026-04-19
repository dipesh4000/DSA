class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        self.findcombination(0, target, candidates, ans, ds)
        return ans
    
    def findcombination(self, index: int, target: int, candidates: List[int], ans, ds):
        if(index >= len(candidates)):
            if(target == 0):
                ans.append(ds[:])
            return
        
        if(candidates[index] <= target):
            ds.append(candidates[index])
            self.findcombination(index, target - candidates[index], candidates, ans, ds)
            ds.pop()

        self.findcombination(index + 1, target, candidates, ans, ds)