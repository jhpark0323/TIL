import git

'''
# 준비사항
# pip install gitpython 한 후에 하면 됩니다

# clone 사용법
# 1. 실습하기 다 눌러놓고 실행하면 됩니당
# 2. 입력예시 : 1 ehdghksdl web C:/Users/SSAFY/Desktop/TIL(그냥 복사하세요) 순서

# add, commit, push 사용법
# 1. 자신이 어떤 과제를 했는지 입력합니다 (과제2, 과제4, 실습1, 실습2, 실습3, 실습4, 실습5, 실습a, 실습b, 실습c)
# 2. 올릴 gitlab의 branch 명을 입력해줍니다
# 3. 올라갑니다

# * 주의사항 *
# 폴더 경로를 입력할 때, 모든 hw, ws의 하나로 모아놓은 상위폴더경로를 복사해주세요(각 과제 폴더들이 한눈에 보이는).
# (add commit push할때, 특정 폴더(hw_1 등)를 입력하면 안됩니다.)
'''

## 온라인 실습실의 자료들을 받아온다 => git으로 클론해온다
## 완성한 파일을 add commit push 한다.

today = int(input('몇일차인지 적어주세요 : '))
user_id = input('깃랩id를 적어주세요 : ')
subject = input('무슨과목인지 적어주세요(소문자) (예시 : web, python...) : ')
user_dir = input("어떤 폴더에서 작업할지 적어주세요 (폴더경로복사) : ")
print('클론할꺼면 1, add commit push 할거면 2를 입력해주세요')
select = int(input())

while True:
    if select == 1:
        ## 온라인 실습실의 자료들을 받아온다 => git으로 클론해온다
        difficulty = [1,2,3,4,5,'a','b','c']
        urlLst = []
        for test in difficulty:
            if test == 2 or test == 4:
                url = f'https://lab.ssafy.com/{user_id}/{subject}_hw_{today}_{test}'
                urlLst.append(url)
                url = f'https://lab.ssafy.com/{user_id}/{subject}_ws_{today}_{test}'
                urlLst.append(url)
            else:
                url = f'https://lab.ssafy.com/{user_id}/{subject}_ws_{today}_{test}'
                urlLst.append(url)
        # 받아올 url 리스트를 만들어 주었다
        for url in urlLst:
            try:
                git.Git(user_dir).clone(url)
                print(f'{url} 의 과제를 {user_dir}로 받아왔습니다')
            except Exception:
                print('실패했슴니다..')
        break
    elif select == 2:
        print('어떤 과제를 수행했는지 입력해주세요 (하나씩 띄어서 입력) ex)과제2 과제4 실습1 실습a 실습b')
        print('*과제는 2 4, 실습은 1 2 3 4 5 a b c 가 있슴니다*')
        my_complete = input()
        branch = input('브랜치 명이 무엇입니까? ex) main, origin ... : ')
        hwLst = my_complete.split()
        completeurlLst = []
        gitUrl = []
        commitM = []
        for hw in hwLst:
            lv = hw[-1]
            if hw[:2] == '과제':
                test = 'hw'
            else:
                test = 'ws'
            completeurlLst.append(f'{user_dir}\{subject}_{test}_{today}_{lv}\.git')
            commitM.append(f'{today}일차_{test}_{lv}단계 제출')
            # 내가 완료한 작업들의 폴더 url이 만들어 졌다
        for idx in range(len(completeurlLst)): # 폴더를 순회한다.
            try:
                repo = git.Repo(completeurlLst[idx])
                repo.git.add(update=True)
                repo.index.commit(commitM[idx])
                origin = repo.remote(name=branch)
                origin.push()
                print(f'"{commitM[idx]}" 을 push 햇슴니다 ^^')
            except Exception:
                print('실패햇슴니다...')
        break
    else:
        print('clone은 1, (add commit push)는 2를 입력해주세요')
        select = int(input())



    
    
