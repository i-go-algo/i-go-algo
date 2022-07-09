# git commit -m "submit : BOJ 01541 잃어버린 괄호 (yoonseok)"
prob = input()
nums = list(map(int,prob.replace('-','+').split('+')))
op = []
for i in prob:
    if i=='+' or i=='-':
        op.append(i)
ans = nums[0]
first = True;
for i,o in enumerate(op):
    if first:
        if o=='+':
            ans+=nums[i+1]
        if o=='-':
            ans-=nums[i+1]
            first = False
    else:
        ans-=nums[i+1]
print(ans)