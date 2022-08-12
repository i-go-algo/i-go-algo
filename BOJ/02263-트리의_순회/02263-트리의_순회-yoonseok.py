# git commit -m "submit : BOJ 02263 트리의 순회 (yoonseok)"
import sys
sys.setrecursionlimit(100000)
N = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
index = [0]*(N+1)
for i in range(N):
    index[inorder[i]]=i
print(index)
def preorder(in_l,in_r,po_l,po_r):
    if in_l>in_r or po_l>po_r:
        return
    
    root = postorder[po_r]
    loc_r = index[root]
    print(root,end = ' ')
    preorder(in_l,loc_r-1,po_l,po_l+(loc_r-in_l)-1)
    preorder(loc_r+1,in_r,po_l+(loc_r-in_l),po_r-1)

preorder(0,N-1,0,N-1)