class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        while numBottles >= numExchange:
            res += numExchange
            numBottles -=numExchange
            numBottles +=1
        return res + numBottles

        # while emptyBottles !=0:
        #     newEmpty =emptyBottles // numExchange
        #     emptyBottles = (filledBottle+ emptyBottles) % numExchange
        #     res += filledBottle
        # return res
        # # numAddRN = numBottles// numExchange
        # # notAddRN = numBottles% numExchange
        # # newNumAddRN = (numAddRN+notAddRN)//numExchange
        # # # notAddRNN = (numAddRN+notAddRN)% numExchange
        # # print((numAddRN+notAddRN), numExchange)
        # # # print(numBottles, numAddRN, newNumAddRN, notAddRNN)
        # # return numBottles+ numAddRN+ newNumAddRN 