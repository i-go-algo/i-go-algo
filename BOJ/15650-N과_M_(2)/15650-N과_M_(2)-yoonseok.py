# git commit -m "submit : BOJ 15650 N과 M (2) (yoonseok)"
def MaN(N, M, start, out):
    if M==0:
        for i in out:
            print(i, end = " ")
        print()
        return
    elif start==N:
        return
    else:
        for i in range(start+1,N+1):
            newout = out[:]
            newout.append(i)
            MaN(N,M-1,i,newout)

N, M = map(int,input().split())
out = []
MaN(N,M,0,out)