class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans= []
        arr = []
        def getset(index: int, arr: List[int]):
            if(index >= len(nums)):
                ans.append(arr)
                return
            getset(index + 1, arr)
            getset(index + 1, arr + [nums[index]])
        getset(0, [])
        return ans