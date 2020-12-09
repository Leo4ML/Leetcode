'''
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # leetcode中仅仅写maxDepth方法即可解答，后面的序列转二叉树函数不用写。
    def maxDepth(self, root: TreeNode) -> int:
        level = 0
        queue = []
        if not root:
            return level
        queue.append(root)
        while queue:
            level += 1
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return level

    def seriesToTree(self, arr: list):
        if not arr:
            return None
        queue = []
        root = TreeNode(arr.pop(0))
        queue.append(root)
        while arr:
            for i in range(len(queue)):
                if arr[0] and arr[1]:
                    queue[0].left = TreeNode(arr.pop(0))
                    queue[0].right = TreeNode(arr.pop(0))
                    queue.append(queue[0].left)
                    queue.append(queue[0].right)
                elif arr[0] or arr[1]:
                    if arr[0]:
                        queue[0].left = TreeNode(arr.pop(0))
                        queue.append(queue[0].left)

                    else:
                        queue[0].right = TreeNode(arr.pop(0))
                        queue.append(queue[0].right)
                else:
                    arr.pop(0)
                    arr.pop(0)
                queue.pop(0)
        return root


arr = [3, 9, 20, None, None, 15, 7]
s = Solution()
r = s.seriesToTree(arr)
print(s.maxDepth(r))
