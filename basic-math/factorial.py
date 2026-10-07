class Solution:
    def factorial(self, n):
        fact = 1
        for i in range(1,n+1):
            fact = fact * i
        return fact    
solution = Solution()
print(solution.factorial(5))    