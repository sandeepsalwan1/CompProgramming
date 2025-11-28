class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack =[]
        res,n =0,len(arr)
        for i in range(n+1):
            while stack and (i==n or arr[i] < arr[stack[-1]]):
                j=stack.pop()
                l=j-(stack[-1] if stack else -1)
                r=i-j
                res= (res+arr[j]*l*r)
            stack.append(i)
    

        return res % (10**9+7)