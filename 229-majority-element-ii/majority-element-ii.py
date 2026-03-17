class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_ele = Counter(nums)
        ans = []

        for item, count in count_ele.most_common():
            if(count <= (len(nums) // 3)):
                break
            ans.append(item)
        return ans