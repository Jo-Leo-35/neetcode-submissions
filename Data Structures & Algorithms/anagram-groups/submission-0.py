class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        for string in strs:
            flag = False
            if res is None:
                res.append([string])
                continue

            for idx, group in enumerate(res):
                if self._Anagrams(group[0], string):
                    group.append(string)
                    flag = True
                    break
                
            if flag is False:    
                res.append([string])
        
        return res

    def _Anagrams(self, s_str:str, t_str:str) -> Bool:
        s_len = len(s_str)
        t_len = len(t_str)
        
        if s_len != t_len:
            return False

        array = [0] * 26

        for s in s_str:
            array[ord(s) - ord("a")] += 1

        for t in t_str:
            array[ord(t) - ord("a")] -= 1

        for a in array:
            if a != 0:
                return False

        return True 