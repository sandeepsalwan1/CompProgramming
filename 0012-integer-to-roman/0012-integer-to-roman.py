
'''listlist contating all cases

iterate reversed order and them check if you can divide it by the current value that youre getting while itrerating. 
    current %= val youre iterating through 




for loop just continue if not 

2500 /1000 = 2
500 = 1 
'''




'''
previous roman numeral + current = current - previous 
hash map of value: numeral 

res =[]
iterate through list 
case 1: not 4/9 then you add val equal to number  
    zeroList = [0] * len(nums) - i
    CurrVal = str(nums[i])
    for i in zeroList:
        CurrVal += i
    CurrVal = int(nums[i])
    take current value and / by maxVal. i would know max val by iterating through values and while val < CurrVal then  say target = val and 
    target[] while target % maxVal > maxVal : res.append(hash[maxVal]) target -= maxVal

case 2: 4/9 follow sub form
    if 4: check next and check prev 


edge cases: if invalid VVVV make sure that my sioliuion can account for numerals that are equal 
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400],["D", 500],["CM", 900],["M", 1000]]
        res = ""
        for romanNum, Val in symList[::-1]:
            if num // Val:
                numTimes=  num // Val
                res += (romanNum * numTimes)
                num %= Val
        return res

        # # for i in num: 
        # res = ""
        # hash = {}
        # hash.update( {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"} ) 
        # num = str(num)
        # for i in range(len(num)):
        #     zeroList = [0] * (len(num) - i-1)
        #     CurrVal = num[i]
        #     for z in zeroList:
        #         CurrVal += str(z)
        #     CurrVal = int(CurrVal)
        #     if CurrVal == 0: continue
        #     while CurrVal > 0:
        #     # target = CurrVal
        #         if CurrVal in [4,9,40,90,400,900]:
        #             if CurrVal == 4: res+=("IV")
        #             elif CurrVal == 40: res+=("XL")
        #             elif CurrVal == 400: res+=("CD")
        #             elif CurrVal == 9: res+=("IX")
        #             elif CurrVal == 90: res+=("XC")
        #             elif CurrVal == 900: res+=("CM")
        #             CurrVal = 0
        #         else:
        #             for k in hash.keys():
        #                 if (k) <= CurrVal:
        #                     maxNum = hash[k]
        #                     maxVal = k
        #                 else: break
        #             res+= (maxNum)
        #             CurrVal -= maxVal

        #             #3749

        #             3000
        #             MMMDCCXLIX
                    



        #     #         check next and check prev 
    


        # return res

