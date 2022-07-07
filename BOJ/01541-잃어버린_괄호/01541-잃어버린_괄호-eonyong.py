# git commit -m "submit : BOJ 01541 잃어버린 괄호 (eonyong)"
# eval 안되는거 에바

calcul = input().split('-')
numbers = []
for cal in calcul:
    if '+' in cal:
        numbers.append(sum(map(int, cal.split('+'))))
    else:
        numbers.append(int(cal))
answer = numbers[0] * 2

for number in numbers:
    answer -= number

print(answer)
