class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        left, right = 1, max(bloomDay)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if self.canMake(bloomDay, m, k, mid):
                right = mid
            else:
                left = mid + 1
        
        return left
    
    def canMake(self, bloomDay, m, k, day):
        bouquets = 0
        flowers = 0
        
        for bloom in bloomDay:
            if bloom <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
                    
                    if bouquets == m:   # 🚀 Early exit
                        return True
            else:
                flowers = 0
                
        return False