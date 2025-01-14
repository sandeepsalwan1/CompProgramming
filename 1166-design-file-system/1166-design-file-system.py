class FileSystem:

    def __init__(self):
        # hash map 
        self.pathDict = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.pathDict: return False
        split,first,count = 0,0,0
        for i in range(len(path)-1,-1,-1):
            if path[i] == "/":
                if first == 0: 
                    split = i
                    first+=1
                count +=1
        if count == 1: 
            self.pathDict[path] = value
            return True
        # add if the substring /leet is in our dict keys 
        prevSubString = path[:split]
        if prevSubString not in self.pathDict: return False
        self.pathDict[path] = value
        return True



    def get(self, path: str) -> int:
        return self.pathDict.get(path,-1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)