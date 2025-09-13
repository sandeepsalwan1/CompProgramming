class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        self.farthest =0
        if s[-1]=="1":return False
        def bfs(cur):
            q = deque([0])
            while q:
                for i in range(len(q)):
                    child=q.popleft()
                    start = max(child+minJump,self.farthest+1)
                    end = min(child+maxJump+1,len(s))

                    for j in range(start,end):
                        if s[j] == "0":
                            if j ==len(s)-1:return True
                            q.append(j)
                    
                    self.farthest = child + maxJump


                    # if s[child]=="1":continue
                    # self.farthest= max(self.farthest,child)
                    # if self.farthest == len(s)-1: return True

                    # for j in range(minJump,maxJump+1):
                    #     if child+j>= len(s): break
                    #     if s[j+child]=="1":continue
                    #     q.append(j+child)
        return True if bfs(0) else False
        return self.farthest ==len(s)-1


        # 0000000

        # 2, 5

        # min = 2..5

        # farthest = 5

        # 4..7

        # 7

        # 8,8