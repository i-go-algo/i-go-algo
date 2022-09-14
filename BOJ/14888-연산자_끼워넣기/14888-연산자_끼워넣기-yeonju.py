def calculation(num, idx, add, subtract, multiply, divide):
    global n, max_value, min_value

    if idx == n:
        max_value = max(num, max_value)
        min_value = min(num, min_value)
        return

    else:
        if add:
            calculation(num + nums[idx], idx + 1, add - 1, subtract, multiply, divide)
        if subtract:
            calculation(num - nums[idx], idx + 1, add, subtract - 1, multiply, divide)
        if multiply:
            calculation(num * nums[idx], idx + 1, add, subtract, multiply - 1, divide)
        if divide:
            if num > 0:
                calculation(num // nums[idx], idx + 1, add, subtract, multiply, divide - 1)
            else:
                calculation(-(-num // nums[idx]), idx + 1, add, subtract, multiply, divide - 1)


n = int(input())

nums = list(map(int, input().split()))
a, b, c, d = map(int, input().split())

max_value = - 10000000000
min_value = 100000000000

calculation(nums[0], 1, a, b, c, d)
print(max_value)
print(min_value)
