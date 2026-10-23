class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        d = {}

        for x in s:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

        for x in t:
            if x in d:
                d[x] -= 1
            else:
                return False
        
        for val in d.values():
            if val != 0:
                return False
        
        return True


