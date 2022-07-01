# git commit -m "submit : BOJ 01541 잃어버린 괄호 (changjun)"


formula = input()
lst = []
flag = 1
tmp_num = ""
for i in formula:
    if i.isnumeric():
        tmp_num += i
    else:
        lst.append(int(tmp_num))
        lst.append(i)
        tmp_num = ""

lst.append(int(tmp_num))
        
ans = lst[0]
flag = 1
tmp = 0
for i in range(1, len(lst), 2):
    if flag:
        if lst[i] == '+':
            ans += lst[i+1]
        else:
            flag = 0
            tmp += lst[i+1]
    else:
        tmp += lst[i+1]
ans -= tmp
print(ans)






# def cal(lst):
#     if lst[1] == '-':
#         return lst[0]-lst[2]
#     else:
#         return lst[0]+lst[2]



# def func(input_lst):
#     l = len(input_lst)
#     if l > 1:
#         for i in range(0, l-2, 2):
#             tmp = cal(input_lst[i:i+3])
#             tmp_lst = input_lst[:]
#             tmp_lst[i:i+3]=[tmp]
#             func(tmp_lst)
#     else:
#         global ans
#         ans = min(ans, input_lst[0])

# ans = float('inf')

# func(lst)
# print(ans)