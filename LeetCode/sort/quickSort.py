def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1


def quickSort(nums, low, high):
    if low < high:
        i = partition(nums, low, high)
        quickSort(nums, 0, i-1)
        quickSort(nums, i+1, high)


nums = [5, 2, 6, 4, 9, 5]
quickSort(nums, 0, len(nums) - 1)
for v in nums:
    print(v)

'''
这里输出结果是5 3， 并不是3 3，说明在交换的时候，并不是先执行a=b,然后执行b = a
应该是a=b,执行b=a的时候，a=b还未交换完，这时候执行b=a，这时候的a还是没有交换完的a
'''
# a, b = 3, 5
# a, b = b, a
# print(a, b)
