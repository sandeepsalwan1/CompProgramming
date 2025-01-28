# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         hash = defaultdict(list)
#         # check [i][j] neighbors 
#         visited = set()
#         self.res = 0
#         def dfs(inputList, inputVal):
#             for i in range len(inputList):
#                 if i != inputVal:
#                     dfs(nums[i], i)
#                     visited.add(nums[i])
#             if inputVal not in visited:
#                 res +=1
# # [1,1,0]
#         for i in range(len(isConnected)):
#             if nums[i] not in visited:
#                 dfs(nums[i],i)
#         return res



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        provinces = 0
        for city in range(n):
            if not visited[city]:
                dfs(city)
                provinces += 1

        return provinces