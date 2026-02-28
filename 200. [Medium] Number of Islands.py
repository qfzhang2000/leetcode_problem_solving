class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ''' For each island, once we find a node, directly loop and label all the other node in this island  (by BFS or DFS)'''
        ''' Time complexity O(nm)'''

        dep = copy.deepcopy(grid)
        ans = 0

        q = deque()

        dx = [-1, 1, 0,  0]
        dy = [0, 0, -1, 1]

        for i in range(0,len(dep)):
            for j in range(0,len(dep[0])):
                if(dep[i][j] == "1"):
                    ans += 1
                    q.append([i,j])
                    dep[i][j] = "0"

                    while(len(q)>0):
                        temp = q.popleft()
                        
                        x=temp[0]
                        y=temp[1]

                        for j in range(len(dx)):
                            if(0<=x+dx[j]<len(dep) and 0<=y+dy[j]<len(dep[0]) and dep[x+dx[j]][y+dy[j]]=="1"):
                                q.append([x+dx[j],y+dy[j]])
                                dep[x+dx[j]][y+dy[j]] = "0"
                
        return ans

                            
