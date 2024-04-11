class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()
        for digit in num:
            while k > 0 and stack and digit < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        for _ in range(k):
            stack.pop()
        
        while stack and stack[0] == '0':
            stack.popleft()
        
        return ''.join(stack) if stack else '0'
