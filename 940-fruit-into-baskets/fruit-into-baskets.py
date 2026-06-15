class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        last = -1
        second_last = -1

        last_count = 0
        curr = 0
        best = 0

        for fruit in fruits:

            if fruit == last or fruit == second_last:
                curr += 1
            else:
                curr = last_count + 1

            if fruit == last:
                last_count += 1
            else:
                last_count = 1
                second_last = last
                last = fruit

            best = max(best, curr)

        return best
# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         basket = {}
#         i = 0
#         maxfruit = 0

#         for j in range(len(fruits)):
#             basket[fruits[j]] = basket.get(fruits[j], 0) + 1

#             while len(basket) > 2:
#                 basket[fruits[i]] -= 1

#                 if basket[fruits[i]] == 0:
#                     del basket[fruits[i]]

#                 i += 1

#             maxfruit = max(maxfruit, j - i + 1)

#         return maxfruit