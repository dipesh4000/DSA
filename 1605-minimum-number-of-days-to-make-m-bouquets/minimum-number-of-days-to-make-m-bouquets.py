class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = min(bloomDay), max(bloomDay)

        if(len(bloomDay) < (m*k)):
            return -1
        if(len(bloomDay) == k):
            return 1
        while(l<r):
            mid = (int)(l + (r-l)//2)
            if(self.candone(bloomDay, m, k, mid)):
                r = mid
            else:
                l = mid + 1
        
        return r
    def candone(self, bloomday: List[int], m: int, k: int, mid: int) -> bool:
        boq_made = 0
        flowers = 0

        for bloom in bloomday:
            if(bloom>mid):
                flowers = 0
            elif(flowers<k):
                flowers += 1
            
            if(flowers == k):
                boq_made += 1
                flowers = 0
        return boq_made >= m