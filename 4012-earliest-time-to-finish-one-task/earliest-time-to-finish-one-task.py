class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        earlyTime = float('inf')

        for task in tasks:
            currTime = sum(task)
            if currTime < earlyTime:
                earlyTime = currTime

        return earlyTime