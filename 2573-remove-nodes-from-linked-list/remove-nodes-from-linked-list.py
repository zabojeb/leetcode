class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        while head:
            while stack and stack[-1].val < head.val:
                stack.pop()
            
            stack.append(head)
            head = head.next
        
        foo = ListNode(0)
        last = foo

        for node in stack:
            last.next = node
            last = last.next
        
        last.next = None

        return foo.next