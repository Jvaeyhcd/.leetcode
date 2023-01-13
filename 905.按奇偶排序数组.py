#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

# @lc code=start
import collections
from turtle import right
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            while left < right and nums[left] % 2 == 0:
                left += 1
            while left < right and nums[right] % 2 == 1:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums
# @lc code=end

def countingSort(arr: List[int], max_value: int) -> List[int]:
    bukect_len = max_value + 1
    bukect = [0] * bukect_len
    for a in arr:
        bukect[a] += 1
    index = 0
    for num in range(bukect_len):
        while bukect[num] > 0:
            arr[index] = num
            index += 1
            bukect[num] -= 1
    return arr


def radixSort(arr: List[int], max_digit: int) -> List[int]:
    mod = 10
    dev = 1
    counter = [[] for _ in range(9)]
    for i in range(max_digit):
        for j in range(len(arr)):
            bukect = (arr[j] % mod) // dev
            counter[bukect].append(arr[j])
        
        pos = 0
        for bukect in range(9):
            while counter[bukect]:
                arr[pos] = counter[bukect].pop(0)
                pos += 1

        mod *= 10
        dev *= 10
    
    return arr


def qiuck_sort(arr: List[int], first: int, last: int):
    if first >= last:
        return
    mid_value = arr[first]
    low = first
    high = last
    while low < high:
        while low < high and arr[high] >= mid_value:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] < mid_value:
            low += 1
        arr[high] = arr[low]

    arr[low] = mid_value
    qiuck_sort(arr, first, low - 1)
    qiuck_sort(arr, low + 1, last)


def merge_sort(arr: List):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left, right = arr[0:mid], arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left: List, right: List):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    while left:
        res.append(left.pop(0))
    while right:
        res.append(right.pop(0))
    return res


def sift_down(arr: List, start: int, end: int):
    parent = start
    child = (parent << 1) + 1
    while child <= end:
        # 先比较两个子节点大小，选择最大的
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        # 如果父节点比子节点大，代表调整完毕，直接跳出函数
        if arr[parent] >= arr[child]:
            return
        else:
            # 否则交换父子内容，子节点再和孙节点比较
            arr[parent], arr[child] = arr[child], arr[parent]
            parent = child
            child = (parent << 1) + 1


def heap_sort(arr: List):
    # 从最后一个节点的父节点开始sift down以完成堆化
    n = len(arr)
    i = (n - 2) // 2
    while i >= 0:
        sift_down(arr, i, n - 1)
        i -= 1
    # 先将第一个元素和已经排好的元素前一位做交换，再重新调整（刚调整的元素之前的元素），直到排序完毕
    i = n - 1
    while i > 0:
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(arr, 0, i - 1)
        i -= 1


def insertion_sort(arr: List):
    for i in range(1, len(arr)):
        j = i - 1
        num = arr[i]
        while j >= 0 and arr[j] > num:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = num


def bucket_sort(arr: List, bucket_size: int):
    n = len(arr)
    max_val, min_val = max(arr), min(arr)
    bucket_count = (max_val - min_val) // bucket_size + 1
    bucket = [[] for _ in range(bucket_count)]
    for num in arr:
        bucket[(num - min_val) // bucket_size].append(num)
    p = 0
    for i in range(bucket_count):
        insertion_sort(bucket[i])
        for j in range(len(bucket[i])):
            arr[p] = bucket[i][j]
            p += 1

def binary_search(arr: List, target: int):
    res = -1
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            res = mid
            break
    return res

N = int(input())
arr = list(map(int, input().split()))
bucket_sort(arr, 3)
print(*arr)
print(binary_search(arr, 4))