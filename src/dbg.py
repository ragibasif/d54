from typing import Any
from ListNode import ListNode
from TreeNode import TreeNode

class dbg:

    def __init__(self) -> None:
        pass

    @staticmethod
    def listnode(head:ListNode|None=None)->str:
        if not head:
            return "None"
        buf:list[str] = []
        curr = head
        seen:set[int] = set()
        bound = 25

        while curr:
            node_id = id(curr)
            if node_id in seen:
                buf.append(f"Cycle({curr.val})")
                break

            seen.add(node_id)
            buf.append(str(curr.val))
            curr = curr.next

            if len(buf) >= bound:
                buf.append("...")
                break

        if not curr and len(buf) < bound + 1:
            buf.append("None")

        res:str = " -> ".join(buf)
        return f"{res}"

    @staticmethod
    def treenode(root:TreeNode|None=None)->str:

        if not root:
            return "None"
        lines:list[str] = []

        def _build(node:TreeNode|None, prefix:str="", is_left:bool=True, is_root:bool=True)->None:
            if node is None:
                label:str = "(L)" if is_left else "(R)"
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

        _build(root)
        return "\n" + "\n".join(lines) + "\n"
    @staticmethod
    def bits(val:int,length:int=8)->str:
        return f"{val:0>{length}b} ({val})"

    @staticmethod
    def matrix(grid:list[list[Any]], path=None)->str:
        if not grid or not grid[0]: return ""

        path_set = set(path) if path else set()
        R, C = len(grid), len(grid[0])

        all_vals:list[str] = []
        for row in grid:
            for val in row:
                all_vals.append(str(val))

        max_data_w = max(len(s) for s in all_vals)
        max_col_idx_w = len(str(C-1))
        cell_w = max(max_data_w, max_col_idx_w)
        full_cell_w = cell_w + 2
        row_idx_w = len(str(R-1))

        buf:list[Any] = []
        header_padding = " " * (row_idx_w + 3)
        header = header_padding + " ".join(str(c).center(full_cell_w) for c in range(C))
        buf.append(header)

        buf.append(" " * (row_idx_w + 2) + "-" * (len(header) - row_idx_w - 2))
        for r, row in enumerate(grid):
            line:list[str] = []
            for c, val in enumerate(row):
                char = str(val)
                display = char.center(cell_w)
                if (r, c) in path_set:
                    line.append(f"[{display}]")
                else:
                    line.append(f" {display} ")
            buf.append(f"{str(r).rjust(row_idx_w)} | {' '.join(line)}")
        return "\n" + "\n".join(buf) + "\n"

