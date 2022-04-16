# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
#           2
#          / \    return True
#         1   3
    def isValidBST(self, node):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node,minVal,maxVal):
            if not node:
                return True
            if node.val <= minVal:
                return False
            if node.val >= maxVal:
                return False

            return helper(node.left, minVal, node.val)  and helper(node.right, node.val, maxVal)
            
        return helper(node, float('-inf'), float('inf'))

root  = TreeNode(5)
node4 = TreeNode(4)
node3 = TreeNode(3)
node6 = TreeNode(6)
node7 = TreeNode(7)

root.left   = node4
root.right  = node6
node6.left  = node3
node6.left  = node3
node6.right = node7

s = Solution()
x = s.isValidBST(root)
print(x)