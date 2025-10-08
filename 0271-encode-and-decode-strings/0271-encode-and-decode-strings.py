class Codec:
    def encode(self, strs: List[str]) -> str:
        if len(strs) ==0: return 
        if len(strs) <=1: return strs[0]
        return "\U0001f44d".join(strs)
        """Encodes a list of strings to a single string.
        """
        

    def decode(self, s: str) -> List[str]:
        # print(s)
        if not s: return [""]
        # if "\U0001f44d" not in s: return list(s)
        res = []
        cur = ""
        for i in range(len(s)):
            if s[i] == "\U0001f44d":
                res.append(cur)
                cur = ""
            else:
                cur+= s[i]
        res.append(cur)
        return res
        
        """Decodes a single string to a list of strings.
        """
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))