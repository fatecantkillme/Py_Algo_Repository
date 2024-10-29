class Solution(object):
    def select_sort(self,nums):
        for i in range(0,len(nums) - 1):
            max_s=i
            for j in range(i+1,len(nums)):
                if nums[j]>nums[max_s]:
                    max_s=j
            if i != max_s:
                nums[i],nums[max_s]=nums[max_s],nums[i]
        return nums
def main():
    nums=[1,2,54,6,8657,3]
    print(nums)
    solution=Solution()
    print(solution.select_sort(nums))
main()