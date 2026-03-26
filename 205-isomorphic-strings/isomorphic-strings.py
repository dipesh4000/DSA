class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st = {}
        map_ts = {}
        
        for i, j in zip(s, t):
            if i in map_st and map_st[i] != j:
                return False
            if j in map_ts and map_ts[j] != i:
                return False
            
            map_st[i] = j
            map_ts[j] = i
        
        return True