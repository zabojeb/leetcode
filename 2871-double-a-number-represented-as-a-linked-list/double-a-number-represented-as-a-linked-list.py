class Solution:
    def doubleIt(self, n: Optional[ListNode]) -> Optional[ListNode]:
        def calculate(n):
            if not n:
                return 0

            q = 2 * n.val + calculate(n.next)
            n.val = q % 10

            return q // 10

        return (n, ListNode(1, n))[calculate(n)]
