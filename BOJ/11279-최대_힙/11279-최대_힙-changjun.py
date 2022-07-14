# git commit -m "submit : BOJ 11279 최대 힙 (changjun)"

from collections import deque
import sys

class Heap: 

    def __init__(self):
        self.val = deque([None])
        self.lenght = 0

 
    def insert(self, x):
        self.lenght += 1
        l = self.lenght
        self.val.append(x)
        while l > 1:
            if self.val[l] > self.val[l//2]:
                self.val[l], self.val[l//2] = self.val[l//2] , self.val[l]
                l = l//2
            else:
                break


    def delete(self):
        if self.lenght == 0:
            print(0)
        elif self.lenght == 1:
            self.lenght -= 1
            print(self.val.pop())
        else:            
            self.lenght -= 1
            print(self.val[1])
            self.val[1] = self.val.pop()
            tmp = 1
            while 1:
                if 2*tmp + 1 <= self.lenght:
                    if self.val[2*tmp] < self.val[2*tmp + 1]:
                        if self.val[tmp] < self.val[2*tmp + 1]:
                            self.val[tmp] ,self.val[2*tmp + 1] = self.val[2*tmp + 1] ,self.val[tmp]
                            tmp = 2*tmp + 1
                            continue
                    else:
                        if self.val[tmp] < self.val[2*tmp]:
                            self.val[tmp] ,self.val[2*tmp] = self.val[2*tmp] ,self.val[tmp]
                            tmp = 2*tmp
                            continue

                elif 2*tmp <= self.lenght:
                    if self.val[tmp] < self.val[2*tmp]:
                        self.val[tmp] ,self.val[2*tmp] = self.val[2*tmp] ,self.val[tmp]
                        tmp = 2*tmp
                        continue
                break

n = int(input())

heap = Heap()
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        heap.delete()
    else:
        heap.insert(x)
