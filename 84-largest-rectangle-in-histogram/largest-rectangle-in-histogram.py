class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        left = [0] * n
        right = [0] * n

        stack = []

        # left boundary
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                stack.pop()

            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)

        stack.clear()

        # right boundary
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            right[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0

        for i in range(n):
            ans = max(ans, heights[i] * (right[i] - left[i]))

        return ans