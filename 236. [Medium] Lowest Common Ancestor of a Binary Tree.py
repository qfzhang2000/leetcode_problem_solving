# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        q_node = deque()
        q_node.append([root, [root]])

        list_p = []
        list_q = []

        while(q_node):
            temp = q_node.popleft()
            temp_node = temp[0]
            temp_val = temp[1]

            if(temp_node == p):
                list_p = temp_val
            if(temp_node == q):
                list_q = temp_val

            l =  temp_node.left
            r =  temp_node.right
            if(not l is None):
                q_node.append([l, temp_val+[l]])      
            if(not r is None):
                q_node.append([r, temp_val+[r]])      
            
        ans = None

        if(len(list_p)>len(list_p)):
            list_p, list_q = list_q, list_p

        # 然后只能从前往后比较公共前缀
        ans = None
        for i in range(min(len(list_p),len(list_q))):
            
            if list_p[i] is list_q[i]:
                ans = list_p[i]
            else:
                break
        return ans
            
        
