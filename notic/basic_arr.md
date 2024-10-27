## python中数组实现方式：列表

列表储存的数据类型可以不一样，数组长度也可以不一致

```python
arr = ["hi",1,[1.7,'a']]	
```

## 基本操作

访问： arr[1]

查找：

```python
def find(nums,val):
    for i in range(len(nums)):
        if val == nums[i]:
            return i
     return -1
```

插入：

```python
nums.append(val)
nums.insert(i,val)
```

删除：

```python
arr.pop()
arr.pop(i)#删除下标i的元素并将所有后面的元素前移
arr.remove(val)#删除值为val的元素
```

## 数组切片

```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])  # 输出: [1, 2, 3]
print(nums[:3])  # 输出: [0, 1, 2]
print(nums[3:])  # 输出: [3, 4, 5]
print(nums[:])   # 输出: [0, 1, 2, 3, 4, 5]
print(nums[::2])  # 输出: [0, 2, 4]
print(nums[1::2]) # 输出: [1, 3, 5]
print(nums[-1])    # 输出: 5
print(nums[-3:])   # 输出: [3, 4, 5]
print(nums[::-1])  # 输出: [5, 4, 3, 2, 1, 0]
```

