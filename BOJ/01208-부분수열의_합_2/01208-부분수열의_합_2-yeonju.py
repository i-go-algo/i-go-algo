from itertools import combinations
from collections import defaultdict


def get_subsequence(li, res):
    for count in range(1, len(nums) + 1):
        for combi in combinations(li, count):
            total_value = sum(combi)
            res[total_value] += 1


n, s = map(int, input().split())
nums = list(map(int, input().split()))

sub_sum1 = defaultdict(int)
sub_sum2 = defaultdict(int)

get_subsequence(nums[n // 2:], sub_sum1)
get_subsequence(nums[:n // 2], sub_sum2)

answer = sub_sum1[s] + sub_sum2[s]

for s1 in sub_sum1:
    if s - s1 in sub_sum2:
        answer += sub_sum1[s1] * sub_sum2[s - s1]
        
print(answer)
