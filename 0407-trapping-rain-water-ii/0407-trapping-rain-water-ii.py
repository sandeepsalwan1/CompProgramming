class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]: return 0
        heap =[]
        if len(heightMap) <  3 or len(heightMap[0]) <  3: return 0
        visited = set()
        m,n = len(heightMap), len(heightMap[0])
        visited= [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1 or j==0 or j==n-1:
                    heapq.heappush(heap, (heightMap[i][j],i,j))
                    visited[i][j] = True
        
        # Track total water trapped
        water = 0
        # Track current water level (starts at minimum boundary height)
        water_level = 0
        # 4-directional movement
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        # Process cells from lowest to highest
        while heap:
            # Pop cell with minimum height
            h, r, c = heapq.heappop(heap)
            # Update water level to max of current level and cell height
            water_level = max(water_level, h)
            
            # Check all 4 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Validate neighbor is in bounds and not visited
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    # Mark neighbor as visited
                    visited[nr][nc] = True
                    # Add trapped water (water_level - actual height)
                    water += max(0, water_level - heightMap[nr][nc])
                    # Add neighbor to heap with its actual height
                    heapq.heappush(heap, (heightMap[nr][nc], nr, nc))
        
        # Return total trapped water
        return water
#         curr barrier cell hiehg

#         seen 

#         heap has 3s

#         addall to heap 

#         pop 3, 0,1
#         neighbor 11 not visited set 
#         then wat level = max(3,2)
#         wattrapped is just 
#         add 3,11 to heap bc thats water level 
#         eventually poop all cells 1,2 water =3-2 =1 


#         1,3 = 3-2 =1 

#         center cell = 2,2 

#         watlevel = 3
#         wat trapped =3 -2 = 1




#         555 
#         5 1 5 
#          555

#     5,0,0
#   501 
#   522

#   5,00
#   01 in heap 10 inheap

#   5,0,1 0,0 in heap 0,2 in heap
#     O(m)
#   wat level = max(5,1)
#   wat traooed +=4asdfasdfasdfasfd

#   retrun wattreappedasdfasdfsadfsadfsdfasfsa