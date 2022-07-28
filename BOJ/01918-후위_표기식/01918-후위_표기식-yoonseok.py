# git commit -m "submit : BOJ 01918 후위 표기식 (yoonseok)"
target = input()
isp = {')':-1,'*':2,'/':2,'+':1,'-':1,'(':0}
icp = {')':-1,'*':2,'/':2,'+':1,'-':1,'(':3}
stack_num=[]
stack_op = []
for c in target:
    if 'A'<=c<='Z':
        stack_num.append(c)
    elif c==')':
        while stack_op and stack_op[-1]!='(':
            stack_num.append(stack_op.pop())
        stack_op.pop()
    elif len(stack_op)==0:
        stack_op.append(c)
    elif isp[stack_op[-1]]>=icp[c]:
        while stack_op and isp[stack_op[-1]]>=icp[c]:
            stack_num.append(stack_op.pop())
        stack_op.append(c)
    else:
        stack_op.append(c)
while stack_op:
    stack_num.append(stack_op.pop())
answer = ''
for i in stack_num:
    answer+=i
print(answer)