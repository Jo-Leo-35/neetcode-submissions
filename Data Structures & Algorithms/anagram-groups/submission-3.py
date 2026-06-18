class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for string in strs:
            tmphash = [0] * 26

            for s in string:
                tmphash[ord(s) - ord("a")] += 1

            hashMap[tuple(tmphash)].append(string)

        return list(hashMap.values())                
                
            