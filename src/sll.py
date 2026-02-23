class ListNode:
    def __init__(self, val=0, next=None)->None:
        self.val = val
        self.next= next

    def __repr__(self)->str:
        return f"ListNode({self.val})"
    def __str__(self)->str:
        if not self:
            return "None"
        buf:list[str] = []
        curr = self
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
