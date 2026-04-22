class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ans = []

        def backtrack(index: int, arr: List[int], sums: int):
            if sums > n:
                return
            if index >= 9:
                if len(arr) == k and sums == n:
                    ans.append(arr[:])
                return
            if(sums < n):
                arr.append(nums[index])
                backtrack(index + 1, arr, sums + nums[index])
                arr.pop()
            backtrack(index + 1,arr, sums)
        
        backtrack(0, [], 0)
        return ans