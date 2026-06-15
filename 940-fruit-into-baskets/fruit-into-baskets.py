class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        i = 0
        maxfruit = 0

        for j in range(len(fruits)):
            basket[fruits[j]] = basket.get(fruits[j], 0) + 1

            while len(basket) > 2:
                basket[fruits[i]] -= 1

                if basket[fruits[i]] == 0:
                    del basket[fruits[i]]

                i += 1

            maxfruit = max(maxfruit, j - i + 1)

        return maxfruit