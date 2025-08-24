class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # totalAdd, oddAdd = divmod(11, 2)
        wordsList = []
        count = 0
        cur = []
        for i, v in enumerate(words):
            if count + len(v) + 1 > maxWidth:
                wordsList.append([cur, maxWidth - count])
                cur = []
                count = 0
            if cur:
                count += len(v) + 1
            else:
                count += len(v)
            cur.append(v)
        if cur:
            wordsList.append([cur, maxWidth - count])
        totalAdd = 0
        for rIdx, i in enumerate(wordsList):
            lis, num = i[0], i[1]
            if rIdx == len(wordsList) - 1:
                i[0][-1] += " " * num
                continue
            if len(lis) == 1:
                i[0][0] += " " * num
                continue
            totalAdd, oddAdd = divmod(num, (len(lis) - 1))
            for idx, j in enumerate(i[0]):
                if idx == len(i[0]) - 1:
                    continue
                i[0][idx] += " " * totalAdd
                if oddAdd:
                    i[0][idx] += " "
                    oddAdd -= 1
        res = []
        for i in wordsList:
            mLis = i[0]
            val = " ".join(mLis)
            if val:
                res.append(val)
        return res
