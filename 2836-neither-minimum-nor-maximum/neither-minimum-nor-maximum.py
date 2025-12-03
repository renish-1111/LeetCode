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


     
        if nums[2] < max_val and nums[2] > min_val:
            return nums[2]
        elif nums[2] > max_val:
            return max_val
        else:
            return min_val

