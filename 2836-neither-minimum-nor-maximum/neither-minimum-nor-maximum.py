class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n < 3:
            return -1

        n1 = nums[0]
        n2 = nums[1]

        if nums[0] > nums[1]:
            max_val = nums[0]
            min_val = nums[1]
        else:
            max_val = nums[1]
            min_val = nums[0]


        for i in range(2,n):
            if nums[i] < max_val and nums[i] > min_val:
                return nums[i]
            elif nums[i] > max_val:
                return max_val
            else:
                return min_val

