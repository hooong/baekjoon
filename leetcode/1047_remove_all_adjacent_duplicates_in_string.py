class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:
            is_unique = True
            while stack:
                if stack[-1] == ch:
                    is_unique = False
                    stack.pop()
                else:
                    break

            if is_unique:
                stack.append(ch)

        return ''.join(stack)
