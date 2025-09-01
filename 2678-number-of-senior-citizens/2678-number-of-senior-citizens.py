class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for i in details:
            # print(details[11:13])
            if int(i[11:13]) > 60: res +=1
        return res