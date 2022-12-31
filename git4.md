# Git4

## merge를 깔끔하게 헤보자

**수많은 branch로 작업할 때 전부 3-way merge하고**  
**그래프를 보면 매우 복잡해보인다 그런게 싫다면 사용하기 좋은 문법**  
※ 참고로 그래프 볼 때는

```
$ git log --graph
```

### **rebase**

브랜치의 시작점을 다른 commit으로 옮기는 방법  
신규 브랜치 시작점을 마스터브랜치 최근 commit으로 옮긴후  
fast-foward merge한다

```
<!-- 1. 새로운 브랜치로 이동 -->
$ git checkout 새로운브랜치

<!-- 2. 최근 마스터 브랜치로 rebase -->
$ git rebase master

<!-- 3. 마스터 브랜치에서 merge하면 끝 -->
$ git merge 새로운브랜치
```

_master말고 다른 브랜치끼리도 가능하다_  
![rebase](https://scaler.com/topics/images/git-rebase-in-git.webp)

### **squash**

rebase랑 비슷하게 쓸 수있는 squash  
이2가지 쓰는 이유 다시 정리하면

- 3-way merge만하면 복잡해보임(그래프복잡)
- git log로 보면 3-way merge로 commit된 내역도 같이나와서 지저분해보임

squash는 master브랜치로 순간이동 하듯이 merge된다  
그래서 3-way처럼 선으로 연결된 모습이 아니라 한줄로보임(그래프)

```
<!-- master에서 3-way merge하듯이 하면되는데 squash붙여주면 된다 -->
$ git merge --squash 합칠브랜치이름

<!-- squash로 합치면 staging area에 있게되어서 마무리로 commit하면 끝 -->
```

이렇게 최종 commit 끝내고 git log로 보면 합쳐진 브랜치내역은 나오지않음

## 시간을 되돌려보자

`버전을 생성하고 합치고 하다가 되돌리고 싶은 순간이 생길 수 있는데`  
그럴 때 사용하는 문법도 알아보자  
많이 쓸지는 모르겠지만..

### **restore**

restore은 파일을 되돌리고 싶을 때 사용

```
<!-- 최근 commit상태로 수정내역 되돌릴 수 있음 -->
$ git restore 파일명

<!-- 입력한 커밋아이디 시점으로 돌아감 -->
$ git restore --sourse 커밋아이디 파일명

<!-- add한 파일을 add취소하고 싶을 때 -->
$ git restore --staged 파일명
```

### **revert**

커밋아이디를 지정해서 그 버전에서 일어난 수정을 다 없애고  
삭제된 새로운 버전으로 만들어준다

```
$ git revert 커밋아이디(커밋아이디 여러개도 가능)
```

이렇게 명령하면 위에글보면 삭제된 버전으로 새로 만든다고했음  
그래서 메세지 다시 적도록 vim에디터가 뜰 건데 메세지 수정하고 닫으면 됨  
i눌러서 메세지 수정하고 나갈거면 esc누르고 :wq치면 수정되져서 저장된다

### **reset**

원하는 커밋아이디를 지정해서 reset할 수 있다
reset은 3가지 옵션이 있는데

1. hard  
   지정된 커밋아이디와 이전 버전을 제외한 버전을 삭제시킨다

2. soft  
   삭제는 아니고 지정된 버전보다 최신버전들을 staging area로 보낸다  
   `다시 고려한뒤 commit할 수 있겠네요`

3. mixed  
   지정된 버전보다 최신버전들을 staging되지 않은 상태로 만든다  
   `다시 고려해보고 add, commit할 수 있겠네요`

_위 3가지 옵션 사용하기_

```
$ git reset --hard 커밋아이디
$ git reset --soft 커밋아이디
$ git reset --mixed 커밋아이디
```

※ git reset 커밋아이디 (그냥 이렇게만 하면 mixed적용됨)  
※ 기록남길 중요한 브랜치는 3-way merge, 아닐때 rebase랑 squash쓰면 좋을듯요
