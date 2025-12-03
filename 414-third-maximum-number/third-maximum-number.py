class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        F = float('-inf')
        S = float('-inf')
        T = float('-inf')

        for num in nums:
            if num > F:
                T = S
                S = F
                F = num
            elif num > S and num != F:
                T = S
                S = num
            elif num > T and num != F and num != S:
                T = num
        
        if T > float('-inf'):
            return T
        else:
            return F
        