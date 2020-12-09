'''
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true

示例 2:
输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false

示例 3:
输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false
'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        queue = [(p, q)]
        while queue:
            tmp1, tmp2 = queue.pop()
            if not tmp1 and not tmp2:
                continue
            if tmp1 and tmp2 and tmp1.val == tmp2.val:
                queue.insert(0,(tmp1.left, tmp2.left))
                queue.insert(0,(tmp1.right, tmp2.right))
            else:
                return False
        return True


s = Solution()

print(s.isSameTree(p, q))
