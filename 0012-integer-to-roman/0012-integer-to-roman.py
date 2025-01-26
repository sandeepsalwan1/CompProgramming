
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
