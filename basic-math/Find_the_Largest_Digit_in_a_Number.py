class Solution:

    def largestdigit(self, n):
        count = 0

        while n > 0:
            res = n % 10

            if res > count:
                count = res

            n = n // 10

        return count


solution = Solution()

print(solution.largestdigit(15437))