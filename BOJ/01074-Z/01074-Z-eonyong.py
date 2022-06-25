# git commit -m "submit : BOJ 01074 Z (eonyong)"
def Z(Sr, Sc, Er, Ec, r, c, cnt):
    # 가장 작은 Z일 경우
    if Ec - Sc == 2:
        s, e = r - Sr, c - Sc
        if s and e:
            print(cnt + 3)
        elif s:
            print(cnt + 2)
        elif e:
            print(cnt + 1)
        else:
            print(cnt)
    else:
        # 2진 탐색 느낌으로 r, c의 범위를 비교
        Mr, Mc = (Sr + Er) // 2, (Sc + Ec) // 2
        if Sr <= r < Mr and Sc <= c < Mc:
            Z(Sr, Sc, Mr, Mc, r, c, cnt)
        elif Sr <= r < Mr:
            Z(Sr, Mc, Mr, Ec, r, c, cnt + (Mr - Sr) ** 2)
        elif Sc <= c < Mc:
            Z(Mr, Sc, Er, Mc, r, c, cnt + 2 * (Mr - Sr) ** 2)
        else:
            Z(Mr, Mc, Er, Ec, r, c, cnt + 3 * (Mr - Sr) ** 2)


n, r, c = map(int, input().split())
powNum = 2 ** n  # 제곱 수
Z(0, 0, powNum, powNum, r, c, 0)
