    
#         [3,0,2,5,4]
#          3 0 2 10 40

#          get(-2)
#          40 / 2




#         null  instead find and replace which is O(n) make new prefixList, in that case you just check if k is greater than length n , where n = len(prefixList) -1, then return 0. otherwise  
# return prefixSum[n - k - 1] / prefixSum[n - 1]



#          5 - 2 -1

#          3 1 2 10 40 
# [] 
# -5 



# [size] - [size-k]
# 2 5 11

# if k elements before 
#          3 1/3
#          0
#          deque([40,10, 2, 0, 3])
class ProductOfNumbers:

    def __init__(self):
        self.prefixSum = [1]
        self.prefixMult = 1
    def add(self, num: int) -> None:
        if num == 0: self.prefixSum, self.prefixMult = [1], 1
        else: 
            self.prefixSum.append(num *self.prefixMult)
            self.prefixMult *= num
    def getProduct(self, k: int) -> int:
        n= len(self.prefixSum) -1
        if k >= len(self.prefixSum): return 0
        return self.prefixSum[-1] // self.prefixSum[-k-1] 


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)