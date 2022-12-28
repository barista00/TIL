# Git

## Git이 뭔가요?

*Git*은 분산버전관리시스템인데 작성한 코드의 버전을 기록하는 도구다  
　`분산버전관리가 뭔가요?` -> 로컬관리저장소만들고 원격저장소를 통해 여럿이서 버전 관리 가능

## 왜 Git써야 되는데요

일반적인 버전 관리는 앞뒤 버전의 차이를 바로 알기 어렵다  
*Git*은 바뀐 버전에 따라 무엇이 다른지 메세지로 알기쉽다  
여러명모여 프로젝트 만들기 편해지겠죠

## Git은 어떻게 쓰고 작동하나요?

*Git*프로그램을 설치하고 VScode terminal(bash선택)에서 명령할 수 있다  
*Git*을 사용하기 위해서 작업할 폴더의 변경사항을 감시하도록 만들어 줘야됨  
`git init`을 터미널에 적고 (master)라는 표기가 나오면 감시 성공  
git init을 쓰면 .git폴더와 로컬저장소가 만들어지는데 이제 버전관리 준비끝이다

이 만든 저장소에서 3가지 구역으로 나눌 수 있는데..  
Working directory (파일내용만 바꾸고 git에 명령을 하지않은 상태 `untracked인 상태`)  
Staging area (**git add**를 명령한 상태, commit할 목록 `staged된 상태`)  
Repository (**git commit**을 명령한 상태 `commited된 상태`)  
※ commited된 상태면 하나의 버전으로 본다

> 파일의 이동 : **Working directory** --add> **staging area** --commit> **reponsitory**

※ 버전업데이트하려면 변경할 파일을 골라 add해서 staging area 몰아 넣어놓고 한방에 commit하면 되겠지요?

**문법**

```
<!-- git 파일, 저장소 만들기 (이거 써야 git쓸 수 있음) -->
git init

<!-- staging area에 변경한 파일 넣기 -->
git add 파일이름

<!-- staging area에 있는 파일을 commit하기 -->
git commit -m '적고싶은메세지'
```

## 현재 파일들이 어디있는지 확인가능?

상태창! **문법**

```
<!-- 현재 기록된 commit보기 -->
git log

<!-- git 저장소 파일체크 (working directory, staging area) -->
git status
```

**`git status`사용시 확인 할 수 있는 알림**

- Nothing to commit, working tree clean (working directory, staging area 둘다 비어있다)

---

**파일상태 확인 가능**

- Untracked files (add하지않은 그냥 untracked인 상태)
- Changes to be commit (commit으로 바뀔 것 add만 한 상태)
- Changed not staged for commit (버전 기록했었음 근데 수정하고 add안함)
