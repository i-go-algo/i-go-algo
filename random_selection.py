import random

print('------------------------------------------------------------')
print('이번 주 문제 개수를 입력해 주세요 !')
print('------------------------------------------------------------')

members = ['준 🐼', '석 🐱', '용 🐉', '쥬 🐰']
n = int(input())

random.shuffle(members)
selected_li = [0]
selected_question = 0

for i in members: 
  while selected_question in selected_li:
    selected_question = random.randint(1, n)

  print(i, ':', selected_question, '번째 문제 당첨 🎉')
  selected_li.append(selected_question)
  
print()
print('축하드립니다 ❗❗✨')
  