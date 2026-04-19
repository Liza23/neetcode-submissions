class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for char in s:
            if char not in s_dict.keys():
                s_dict[char] = 0
            s_dict[char] += 1
        
        for char in t:
            if char not in s_dict.keys():
                return False
            s_dict[char] -= 1
        
        for char in s_dict.keys():
            if s_dict[char] > 0:
                return False
        
        return True