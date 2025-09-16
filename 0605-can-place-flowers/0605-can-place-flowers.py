class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = False
        for v,i in enumerate(flowerbed):
            if i == 1:
                prev = True
            else:
                if prev: 
                    prev = False
                else:
                    if v == len(flowerbed)-1:
                        n-=1
                        prev = True
                    else:
                        if flowerbed[v+1]==1:
                            continue
                        else:
                            n-=1
                            prev = True

        return n<=0