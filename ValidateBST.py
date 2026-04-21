class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minimum, maximum):
            if not root:
                return True
            
            if minimum >= root.val or maximum <= root.val:
                return False
            
            return dfs(root.left, minimum, root.val) and dfs(root.right, root.val, maximum)

        return dfs(root, float('-inf'), float('inf'))
