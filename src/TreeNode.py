class TreeNode:
    def __init__(self, val:int=0, left=None, right=None)->None:
        self.val:int = val
        self.left = left
        self.right = right

    def __repr__(self)->str:
        left_val = self.left.val if self.left else "null"
        right_val = self.right.val if self.right else "null"
        return f"TreeNode({self.val}, L:{left_val}, R:{right_val})"