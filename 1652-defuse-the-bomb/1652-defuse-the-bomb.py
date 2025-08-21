class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0: return [0]*len(code)
        # if 
        # code.popleft()
        # code.append(code.copy())
        res = [0]*len(code)
        step=  abs(k) % len(code)
        for i in range(len(code)):
            # print((i+k)%len(code))
            # print(code[i:(i+k)%len(code)])
            if k >0:
                res[i] = sum(code[(i+j)%len(code)] for j in range(1,step+1))
            else:
                res[i] = sum(code[(i-j)%len(code)] for j in range(1,step+1))
            # else: code[i] = code[]

        return res