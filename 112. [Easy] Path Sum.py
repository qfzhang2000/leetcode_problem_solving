# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        '''This is a simple recusion problem'''
        '''Note that a leaf node is the node without child node'''
      
        def iterLoop(cur_val, root):
            if(root is None):
                return False
            if(root.left is None and root.right is None):
                if(cur_val + root.val == targetSum):
                    return True
                else:
                    return False
            else:
                return (iterLoop(cur_val + root.val, root.left) or iterLoop(cur_val + root.val, root.right))

        if(not root is None):
            return iterLoop(0, root)
        else:
            return False
