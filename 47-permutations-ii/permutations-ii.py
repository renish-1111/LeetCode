class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        self.parm(nums,sub,res)
        return list(res)
    
    def parm(self,nums,sub,res):
        if not nums:
            res.append(sub)
        used = set()
        for i in range(len(nums)):
            if nums[i] in used:
                continue
            used.add(nums[i])
            ch = nums[i]
            newnums = nums[:i]+nums[i+1:]
            self.parm(newnums,sub+[ch],res)