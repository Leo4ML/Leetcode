'''
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            n = len(queue)
            tmp = []
            for _ in range(n):
                node = queue.pop()
                tmp.insert(0, node.val)
                if node.right:
                    queue.insert(0,node.right)
                if node.left:
                    queue.insert(0,node.left)
            res.append(tmp)
        return res