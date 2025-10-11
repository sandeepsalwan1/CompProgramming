class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # totalAdd, oddAdd = divmod(11, 2)
        wordsList = []
        count = 0
        cur = []
        for i, v in enumerate(words):
            print(wordsList)
            if count + len(v) >= maxWidth:
                wordsList.append([cur, maxWidth - count])
                cur = []
                count = 0
            if cur:
                count += len(v) + 1
            else:
                count += len(v)
            cur.append(v)
        wordsList.append([cur, maxWidth - count])
        print(cur, wordsList)
        for rIdx, i in enumerate(wordsList):
            lis, num = i[0], i[1]
            if rIdx == len(wordsList) - 1 or len(lis) == 1:
                i[0][-1] += " " * num
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
