class Solution: 
 
    def primeUptoN(self, n): 
 
        if n < 2: 
            return 0 
 
        is_prime = [True] * (n + 1) 
 
        is_prime[0] = False 
        is_prime[1] = False 
 
        p = 2 
 
        while p * p <= n: 
 
            if is_prime[p]: 
 
                for multiple in range(p * p, n + 1, p): 
                    is_prime[multiple] = False 
 
            p += 1 
 
        return sum(is_prime) 
solution = Solution() 
print(solution.primeUptoN(10))   