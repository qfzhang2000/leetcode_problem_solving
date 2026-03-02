"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        '''Practice map''

        if(node is None):
            return None

        mp = {node: Node(node.val, [])}

        q = deque()
        q.append(node)

        while(q):
            x = q.popleft()
            cur_new_node = mp[x]

            for v in x.neighbors:
                if(v not in mp):
                    q.append(v)
                    mp[v] = Node(v.val,[])
                cur_new_node.neighbors.append(mp[v])
                
        return mp[node]
