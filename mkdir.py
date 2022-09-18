import os

# ----------------------------------------------------------------------------------
print('------------------------------------------------------------')
print('노션 테이블의 [문제번호][문제 이름]를 복붙 후 ENTER 2번 눌러주세요.')
print('------------------------------------------------------------')

datas = []

while True:
    data = input().split()

    if data:
        datas.append(data)
    else:
        input('위 문제들로 디렉토리를 생성하겠어요? (ENTER)')
        break

prob_lst = []

for data in datas:
    num = data.pop(0).zfill(5)
    title = ' '.join(data)
    title_bar = title.replace(' ', '_')

    problem = f'{num}-{title_bar}'
    path = f'./BOJ/{problem}' 

    readme = f"# {str(int(num))} {title}\nhttps://www.acmicpc.net/problem/{num}"

# ----------------------------------------------------------------------------------

    # 디렉토리 생성
    if not os.path.exists(path):
        os.makedirs(path)
        # 개별 파일 생성
        members = ['eonyong', 'yeonju', 'yoonseok']

        for member in members:
            filepath = os.path.join(path, f'{problem}-{member}.py')
            fid = open(filepath, 'w', encoding='utf8')
            fid.write(f'# git commit -m "submit : BOJ {num} {title} ({member})"')
            fid.close()

        # README 생성
        md_path = os.path.join(path, 'README.md')
        md_fid = open(md_path, 'w', encoding='utf8')
        md_fid.write(readme)
        md_fid.close()

        print(f'{num} 디렉토리 생성 끝!')
        prob_lst.append(problem)
    else:
        print(f'{num} 이미 존재하는 디렉토리입니다.')

with open('./.github/PULL_REQUEST_TEMPLATE.md', 'w', encoding='utf8') as f:
    f.write('## 💡 Idea & Algorithm <!-- 핵심 아이디어 및 알고리즘 -->\n')
    for prob in prob_lst:
        f.write(f'### {prob}  \n')
    f.write('## 💬 Comment <!-- 후기 -->\n')
