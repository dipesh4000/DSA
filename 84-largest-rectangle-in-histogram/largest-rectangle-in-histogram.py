class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        ans = 0

        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ans = max(ans, height * width)

            stack.append(i)

        n = len(heights)

        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = n - stack[-1] - 1
            ans = max(ans, height * width)

        return ans

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         n = len(heights)

#         left = [0] * n
#         right = [0] * n

#         stack = []

#         # left boundary
#         for i in range(n):
#             while stack and heights[stack[-1]] > heights[i]:
#                 stack.pop()

#             left[i] = stack[-1] + 1 if stack else 0
#             stack.append(i)

#         stack.clear()

#         # right boundary
#         for i in range(n - 1, -1, -1):
#             while stack and heights[stack[-1]] >= heights[i]:
#                 stack.pop()

#             right[i] = stack[-1] if stack else n
#             stack.append(i)

#         ans = 0

#         for i in range(n):
#             ans = max(ans, heights[i] * (right[i] - left[i]))

#         return ans