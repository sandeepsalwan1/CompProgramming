class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l,r = 0, len(cardPoints)-k
        totalP = sum(cardPoints)
        sumV = sum(cardPoints[l:r])
        maxSum =  totalP - sumV

        while r < len(cardPoints):
            sumV -= cardPoints[l]
            sumV += cardPoints[r]
            maxSum = max(totalP - sumV,maxSum)
            l,r = l+1,r+1
        return maxSum
        # [1,2,3,4,5,6,1]
        #      0
        #              1
        # 18
        # 18
        # # take top or botoom 
        # @cache
        # def dp(l,r, ko):
        #     if ko == 0: 
        #         return 0
        #     return max (cardPoints[r]+ dp(l, r-1, ko-1), cardPoints[l]+ dp(l+1, r, ko-1))

        # return dp(0,len(cardPoints)-1, k)
