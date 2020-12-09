'''
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''
# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.appendleft(root)
        tree = []
        tree.append([root.val])
        while queue:
            n = len(queue)
            tmp = []
            for _ in range(n):
                cur = queue.pop()
                if cur.left:
                    queue.appendleft(cur.left)
                    tmp.append(cur.left.val)
                if cur.right:
                    queue.appendleft(cur.right)
                    tmp.append(cur.right.val)
            tree.append(tmp)
        res = []
        for i in range(len(tree)):
            if tree[i]:
                res.append(tree[i][-1])
        return res
'''


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return
            if depth>len(res):
                res.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        dfs(root, 1)
        return res


nums = [1, 2, 3, None, 5, None, 4]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
s = Solution()
print(s.rightSideView(root))
