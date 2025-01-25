
class Solution:
    def intToRoman(self, num: int) -> str:
        # for i in num: 
        res = ""
        hash = {}
        hash.update( {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"} ) 
        num = str(num)
        # 2500
        # M
        # 1000

        for i in range(len(num)):
            zeroList = [0] * (len(num) - i-1)
            CurrVal = num[i]
            for z in zeroList:
                CurrVal += str(z)
            CurrVal = int(CurrVal)
            if CurrVal == 0: continue
            while CurrVal > 0:
            # target = CurrVal
                if CurrVal in [4,9,40,90,400,900]:
                    if CurrVal == 4: res+=("IV")
                    elif CurrVal == 40: res+=("XL")
                    elif CurrVal == 400: res+=("CD")
                    elif CurrVal == 9: res+=("IX")
                    elif CurrVal == 90: res+=("XC")
                    elif CurrVal == 900: res+=("CM")
                    CurrVal = 0
                else:
                    target = CurrVal
                    maxNum = "I"
                    maxVal = 0
                    for k in hash.keys():
                        if (k) <= CurrVal:
                            maxNum = hash[k]
                            maxVal = k
                        # else: break
                        # while target >= maxVal and maxVal!= 0:
                    res+= (maxNum)
                    CurrVal -= maxVal

            #         check next and check prev 
    


        return res

