class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
    
        if len(s) != len(t):
            return False
        else:
            for i in s:
                if i not in s_map:
                    s_map[i] = 1
                s_map[i] += 1

            for j in t:
                if j not in t_map:
                    t_map[j] = 1
                t_map[j] += 1
                
            if s_map == t_map:
                return True

            return False
            