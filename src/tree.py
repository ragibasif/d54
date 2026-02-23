class TreeNode:
    def __init__(self, val:int=0, left=None, right=None)->None:
        self.val:int = val
        self.left = left
        self.right = right

    def __repr__(self)->str:
        left_val = self.left.val if self.left else "null"
        right_val = self.right.val if self.right else "null"
        return f"TreeNode({self.val}, L:{left_val}, R:{right_val})"

    def __str__(self)->str:

        if not self:
            return "None"
        lines = []

        def _build(node, prefix="", is_left=True, is_root=True):
            if node is None:
                label = "(L)" if is_left else "(R)"
                # Using \-- for bottom (left) and /-- for top (right)
                connector = "\\-- " if is_left else "/-- "
                lines.append(f"{prefix}{connector}{label} [N]")
                return

            if node.right or node.left:
                _build(
                    node.right,
                    prefix + ("|       " if is_left and not is_root else "        "),
                    False,
                    False,
                )

            if is_root:
                connector = "ROOT--- "
            else:
                label = "(L)" if is_left else "(R)"
                connector = "\\-- " if is_left else "/-- "
                connector += label + " "

            lines.append(f"{prefix}{connector}{node.val}")

            if node.left or node.right:
                _build(
                    node.left,
                    prefix + ("        " if is_left or is_root else "|       "),
                    True,
                    False,
                )

        _build(self)
        return "\n" + "\n".join(lines) + "\n"

