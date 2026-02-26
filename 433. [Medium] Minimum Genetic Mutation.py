class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        '''As all the mutation only has one distance |x-y|_{0}, we could easily judget whether mutation is feasible'''
        '''This minimal step has a typical BFS solution'''
      
        def feas_mut(a: str, b: str) -> bool:
            cnt = 0
            for i in range(0,len(a)):
                if(not a[i] == b[i]):
                    cnt += 1
            
            return (cnt==1)


        b = [True for _ in range(0,len(bank))]
        q =  deque()
        q.append([startGene, 0])

        while(len(q)>0):
            val = q.popleft()
            s_temp = val[0]
            s_step = val[1]

            if(s_temp == endGene):
                return s_step

            for i in range(0,len(bank)):
                if(b[i] and feas_mut(s_temp, bank[i])):
                    q.append([bank[i], s_step+1])
                    b[i] = False
            
        return -1
