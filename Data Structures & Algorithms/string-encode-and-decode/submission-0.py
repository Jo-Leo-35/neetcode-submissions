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
            if s[i].isdigit():                       # 還在讀長度數字
                num += s[i]                          # 累積(不是 join！)
                i += 1
            elif s[i] == "#":                        # 分隔符:後面接 int(num) 個字元
                index = int(num)
                array.append(s[i+1 : i + index + 1]) # 你這行已經對了
                i += index + 1                       # 跳過 '#' 和那段內容
                num = ""                             # 重置,準備讀下一段
            # 內容字元會被上面 i += index+1 直接跳過,不會單獨走到這

        return array