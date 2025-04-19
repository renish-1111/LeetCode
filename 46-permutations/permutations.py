class Solution:


    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        self.parm(nums,sub,res)
        return res

    def parm(self,nums,sub,res):
        if not nums:
            res.append(sub)
        for i in range(len(nums)):
            ch = nums[i]
            newnums = nums[:i] + nums[i+1:]
            self.parm(newnums,sub+[ch],res)