class Solution:
    def bubbleSort(self, nums):
        for i in range(len(nums)-1):
            for j in range(0, len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

def main():
    nums = [1, 2, 4, 2, 2, 1]
    print("Original list:", nums)
    solution = Solution()  # 创建Solution类的实例
    sorted_nums = solution.bubbleSort(nums)  # 通过实例调用bubbleSort方法
    print("Sorted list:", sorted_nums)

main()