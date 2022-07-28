# git commit -m "submit : BOJ 01991 트리 순회 (yoonseok)"
N= int(input())
tree = list([] for i in range(26))
for i in range(N):
    p, c1,c2 = input().split()
    tree[ord(p)-ord('A')].append(ord(c1)-ord('A'))
    tree[ord(p)-ord('A')].append(ord(c2)-ord('A'))
def preorder(root):
    print(chr(root+ord('A')), end = '')
    if tree[root][0]!=ord('.')-ord('A'):
        preorder(tree[root][0])
    if tree[root][1]!=ord('.')-ord('A'):
        preorder(tree[root][1])
def inorder(root):
    if tree[root][0]!=ord('.')-ord('A'):
        inorder(tree[root][0])
    print(chr(root+ord('A')),end = '')
    if tree[root][1]!=ord('.')-ord('A'):
        inorder(tree[root][1])
def postorder(root):
    if tree[root][0]!=ord('.')-ord('A'):
        postorder(tree[root][0])
    if tree[root][1]!=ord('.')-ord('A'):
        postorder(tree[root][1])
    print(chr(root+ord('A')),end='')
preorder(0)
print()
inorder(0)
print()
postorder(0)
