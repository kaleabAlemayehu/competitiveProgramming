# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def rec(l,r):
            if r < l:
                return None
            m = (r + l)//2
            root = TreeNode(nums[m])
            root.left = rec(l, m-1)
            root.right = rec(m+1, r)
            return root
        
        return rec(0, len(nums)-1)



