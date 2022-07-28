nums = []
n = int(input())
for _ in range(n):
    nums.append(list(map(int, input().split())))

for row in range(n):
    for i in range(row + 1):

        if row == 0:
            continue

        elif row == 1:
            nums[row][i] += nums[0][0]

        else:
            if i == 0:
                nums[row][i] += nums[row - 1][i]
            elif i == row:
                nums[row][i] += nums[row - 1][i - 1]
            else:
                nums[row][i] += max(nums[row - 1][i - 1], nums[row - 1][i])

print(max(nums[-1]))

