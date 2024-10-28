class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        flage=[]
        all=1
        res=[]
        for i in range(len(nums)):
            if nums[i]==0:
                flage.append(i)
            else:
                all=all*nums[i]
        if len(flage)>1:
            res=[0]*len(nums)
        if len(flage)==1:
            res=[0]*len(nums)
            res[flage[0]]=all
        if len(flage)==0:
            for i in range(len(nums)):
                res.append(int(all/nums[i]))
        return res