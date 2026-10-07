class Solution:

    def odd_digits(self, n):
        count = 0

        while n > 0:
            res = n % 10

            if res % 2 != 0:
                count += 1

            n = n // 10

        return count


solution = Solution()

print(solution.odd_digits(154379))