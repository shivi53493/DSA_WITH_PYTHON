def kadane(arr):
    max_sum = float('-inf')
    curr_sum =0
    for num in arr:
        curr_sum = max(num,curr_sum+num)
        max_sum = max(max_sum,curr_sum)

    return max_sum
arr = [-1,-3,-4,10]
print(kadane(arr))