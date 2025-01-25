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
        hash = {}
        # for i in num: 
        hash.update( {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"} ) 
        res = ""
        num = str(num)
        for i in range(len(num)):
            zeroList = [0] * (len(num) - i-1)
            CurrVal = num[i]
            for i in zeroList:
                CurrVal += str(i)
            CurrVal = int(CurrVal)
            if CurrVal == 0: continue
            maxNum = "I"
            
            maxVal = 0
            for k in hash.keys():
                if (k) <= CurrVal:
                    maxNum = hash[k]
                    maxVal = k
                else: break
            print(maxNum, maxVal)


            target = CurrVal
            if CurrVal in [4,9,40,90,400,900]:
                if CurrVal == 4: res+=("IV")
                elif CurrVal == 40: res+=("XL")
                elif CurrVal == 400: res+=("CD")
                elif CurrVal == 9: res+=("IX")
                elif CurrVal == 90: res+=("XC")
                elif CurrVal == 900: res+=("CM")
            elif maxNum in ["V","L","D"]:
                # carryOver = maxVal
                res += (maxNum)
                # carryOver -= maxVal 
                continue
            else:
                target = CurrVal
                while target >= maxVal and maxVal!= 0:
                    res+= (maxNum)
                    target -= maxVal

        #         check next and check prev 
 


        return res

