class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        s = [0, 0]

        cur_idx = 0
        cnt = len(matrix)*len(matrix[0])

        d1 = [0, 1, 0, -1]
        d2 = [1, 0, -1, 0]

        visit = [[True for c in range(len(matrix[0]))] for c in range(len(matrix))]


        ans = []

        while(True):
            print(s)
            visit[s[0]][s[1]] = False
            ans.append(matrix[s[0]][s[1]])
            cnt = cnt - 1

            if(cnt == 0):
                break

            if(not( 0<=s[0]+d1[cur_idx]<len(matrix) and  0<= s[1]+d2[cur_idx]<len(matrix[0]))):
                cur_idx = (cur_idx+1) % 4
            elif(not visit[s[0]+d1[cur_idx]][s[1]+d2[cur_idx]]):
                cur_idx = (cur_idx+1) % 4

            s = [s[0]+d1[cur_idx], s[1]+d2[cur_idx]]
        
        return ans
        
