# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        vis = []
        if not root:
            return 0
        stack.append(root)
        while stack:
            curr = stack.pop()
            if curr not in vis:
                if curr.right:
                    stack.append(curr.right)

                if curr.left:
                    stack.append(curr.left)

                vis.append(curr)
        
            else:
                stack.pop()

        return (len(vis))

root  = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)


root.left = node2
root.right =  node3
node2.left =  node4
node2.right =  node5





t = Solution()


t.countNodes(root)



