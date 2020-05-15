def countSort(arr, res, k):
    count = [0]*(k+1)
    for i in arr:
        count[i] += 1
    for i in range(1, k+1):
        count[i] += count[i-1]
    for i in range(len(arr)-1, -1, -1):
        res[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    return res
nums = [5, 2, 6, 4, 9, 5]
res = [0]*len(nums)
countSort(nums, res, 9)
for v in res:
    print(v)