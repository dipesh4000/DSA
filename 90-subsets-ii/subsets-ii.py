class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(index: int, arr: List[int]):
            ans.append(arr[:])
            if(index == len(nums)):
                return
            for i in range(index, len(nums)):
                if(i >  index and nums[i] == nums[i - 1]):
                    continue
                arr.append(nums[i])
                backtrack(i + 1, arr)
                arr.pop()
        backtrack(0, [])
        return ans