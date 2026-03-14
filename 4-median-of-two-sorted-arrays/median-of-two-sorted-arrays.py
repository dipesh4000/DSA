class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        size = len(nums1)
        if(size>1):
            index = size//2
            if(size%2 == 0):
                return (nums1[index - 1] + nums1[index])/2
            else:
                return nums1[index]
        return nums1[0]