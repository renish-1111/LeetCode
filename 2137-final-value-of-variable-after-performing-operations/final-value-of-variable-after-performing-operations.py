class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum = 0 
        for o in operations:
            if o == "++X" or o == "X++":
                sum+=1
            else:
                sum-=1
        return sum