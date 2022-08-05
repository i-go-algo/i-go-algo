# git commit -m "submit : BOJ 09251 LCS (yoonseok)"
a = input()
b = input()
a = "0"+a
b = "0"+b
la = len(a)
lb = len(b)
table = [[0]*lb for i in range(la)]
for i in range(1,la):
    for j in range(1,lb):
        if a[i]==b[j]:
            table[i][j] = table[i-1][j-1]+1
        else:
            if table[i-1][j] > table[i][j-1]:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i][j-1]

print(table[la-1][lb-1])
