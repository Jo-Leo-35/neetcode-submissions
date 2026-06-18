class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ""
        
        for string in strs:
            num = len(string)
            add = str(num) + "#" + string
            encode_string = encode_string + add
        
        return encode_string
    
    def decode(self, s: str) -> List[str]:
        array = []
        num = ""
        i = 0

        while i < len(s):
            if s[i].isdigit():
                num = num + str(s[i])
                i +=1
    
            if s[i] == "#":
                length = int(num)
                array.append(s[i+1 : i + 1 + length])
                i += length + 1
                num = ""
            
        return array