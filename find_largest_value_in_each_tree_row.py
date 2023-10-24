# find largest value in each tree row
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]
        queue=deque([root])
        while queue:
            maxi=queue[0].val
            for _ in range(len(queue)):
                node=queue.popleft()
                maxi=max(maxi,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(maxi)
        return res
            
