class Solution:
    def isperfect(self, n: int) -> bool:

        total = 0

        for i in range(1, n):
            if n % i == 0:
                total += i

        return total == n
solution = Solution()
print(solution.isperfect(6))    