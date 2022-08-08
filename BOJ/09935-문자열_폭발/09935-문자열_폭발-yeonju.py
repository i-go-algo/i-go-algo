words = input()
explosive_word = list(input())
st = []

for word in words:
    st.append(word)

    if word == explosive_word[-1]:
        if st[len(st) - len(explosive_word): len(st)] == explosive_word:
            for _ in range(len(explosive_word)):
                st.pop()

if st:
    print(''.join(st))
else:
    print('FRULA')
