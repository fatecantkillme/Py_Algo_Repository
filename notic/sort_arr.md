# 冒泡bubbleSort

```
基本思想：相邻元素比较，较大或者较小元素向一侧靠拢
```



```python
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
```

# 选择selection_Sort



```
每次选择一个位置在未排序区选一个合适的
```



```python
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
```

# 插入Insertion_Sort

```
基本思想：分为左有序区右无序区，每次用无序区的元素找有序区
```

