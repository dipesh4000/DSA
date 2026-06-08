class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greator_pivot = []
        smaller_pivot = []
        pivota = []
        for n in nums:
            if(n > pivot):
                greator_pivot.append(n)
            elif(n < pivot):
                smaller_pivot.append(n)
            else:
                pivota.append(n)
        return smaller_pivot + pivota + greator_pivot
        # greator_pivot = []
        # smaller_pivot = []
        # pivota = []
        # i= j= 0
        # while(j < len(nums)):

        # return smaller_pivot + pivota + greator_pivot
