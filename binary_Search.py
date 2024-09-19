def search(num: list[int], target: int):
    l = 0
    r = len(num) - 1
    while l<=r:
        m = (l+r)//2
        if target == num[m]:
            return m
        elif target > num[m]:
            l = m + 1
        elif target < num[m]:
            l = m - 1
    return -1

num_list = [-3,0,5,6,9,10]
target_value = 5
result = search(num_list, target_value)
print(f"Index of {target_value}: {result}")
