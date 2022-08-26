# git commit -m "submit : BOJ 15652 N과 M (4) (yoonseok)"
def MaN(N, M, start, out):
    if M==0:
        for i in out:
            print(i, end = " ")
        print()
        return
    
    else:
        for i in range(start,N+1):
            newout = out[:]
            newout.append(i)
            MaN(N,M-1,i,newout)

N, M = map(int,input().split())
out = []
MaN(N,M,1,out)