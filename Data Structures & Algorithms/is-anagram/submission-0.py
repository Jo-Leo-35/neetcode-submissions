from typing import defaultdict 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array = [0] * 26
        for char in s:
            array[ord(char) - ord("a")] += 1
        
        for char in t:
            array[ord(char) - ord("a")] -= 1
        
        for i in range(0,26):
            if array[i] != 0:
                return False
        
        return True
                