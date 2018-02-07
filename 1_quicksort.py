# 快速排序基本思想是：
# 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
# 然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

# 如序列[6，8，1，4，3，9]，选择6作为基准数。从右向左扫描，寻找比基准数小的数字为3，交换6和3的位置，
# [3，8，1，4，6，9]，接着从左向右扫描，寻找比基准数大的数字为8，交换6和8的位置，[3，6，1，4，8，9]。
# 重复上述过程，直到基准数左边的数字都比其小，右边的数字都比其大。然后分别对基准数左边和右边的序列递归进行上述方法。


def parttion(arr, left, right):
    # 基准值
    key = arr[left]
    # 左边界
    low = left
    # 右边界
    high = right
    while low < high:
        while (low < high) and (arr[high] >= key):
            high -= 1
        arr[low] = arr[high]
        while (low < high) and (arr[low] <= key):
            low += 1
        arr[high] = arr[low]
        arr[low] = key
    return low


def quicksort(arr, left, right):
    if left < right:
        p = parttion(arr, left, right)
        quicksort(arr, left, p - 1)
        quicksort(arr, p + 1, right)
    return arr


s = [6, 8, 1, 4, 3, 9, 5, 4, 11, 2, 2, 15, 6]
print("before sort:", s)
s1 = quicksort(s, left=0, right=len(s) - 1)
print("after sort:", s1)

a = list(input('请输入序列：'))
print("before sort:", a)
a1 = quicksort(a, left=0, right=len(a) - 1)
print("after sort:", a1)
