class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        cnt = s.count(letter)
        n = len(s)
        stack = []

        for i,c in enumerate(s):
            while stack and (c < stack[-1] and len(stack) + n - i > k and (stack[-1] != letter or cnt > repetition)) or k - len(stack) < repetition:
                cur = stack.pop()
                if cur == letter:
                    repetition += 1

            if len(stack) < k:
                stack.append(c)
                if c == letter:
                    repetition -= 1

            if c == letter:
                cnt -= 1

        return ''.join(stack[:k])
               