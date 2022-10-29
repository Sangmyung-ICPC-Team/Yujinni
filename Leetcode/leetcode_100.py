#leetcode 100 graph question
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #만약 두개의 값이 null이 나온다면 true로 반환
            return True
        elif not p or not q or p.val!=q.val: #만약 하나라도 null이 나오거나 값이 어긋나게 되면 false로 반환
            return False
        if p.val==q.val: 만약 값이 같으면
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) #계속 아래것을 비교를 해준다.
