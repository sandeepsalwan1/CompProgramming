class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in words:
            for idx,v in enumerate(words):
                if v == i: continue
                if i in v: 
                    res.append(i)
                    break


        return res