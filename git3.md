# Git3

## **branch란**

독립적인 작업공간을 이용해 하나의 프로젝트를 여러명이 겹치지않게  
작업이 가능하도록 하는 개념  
~~굵은 메인 나무가지에 얇은 잔가지 나는 느낌~~

만약 master라는 branch에서 a파일을 작업중인데,  
background라는 branch에서 a파일을 작업해도 합치지만 않으면  
master파일 변화가 생기지 않는다

> 즉, branch를 잘 활용하면 여러명이 같이 작업해도 혼선이 생기지 않는다

## **branch주요명령어**

- branch 생성

```
$ git branch 브랜치이름
```

- branch 이동

```
$ git checkout 이동할브랜치이름
```

- branch 생성하면서 바로 이동하기

```
$ git checkout -b 브랜치이름
```

- branch 목록 들여다보기

```
$ git branch
```

- branch 삭제

```
$ git branch -d 삭제할브랜치이름
```

`브랜치를 생성하고 각자 자기일하고 다 했으면 작업한거 합쳐야지 그래야 팀웍이고 협업이지 merge를 배워보자`

## **merge**

다른 브랜치에서 작업된 것을 합칠 때 사용하는 명령  
메인이 되는 브랜치에서 명령해주면 된다

```
$ git merge 브랜치이름
```

--------------**잠깐!** 병합할 때 2가지 엔딩이 있는데

- 각각의 브랜치에서 _다른_ 파일을 수정한 경우
- 각각의 브랜치에서 _같은_ 파일을 수정한 경우  
  **첫번째**의 경우 그냥 잘만 병합이 되고 커밋된다  
  **두번째**의 경우 충돌이 일어난다(merge conflict)  
  그럼 너한테 물어본다 `겹치는거 있는데 둘중 뭐 선택해서 병합할까??`  
  수정하고 add, commit하면 된다

그리고 merge될 때 합쳐지는 방법도 나뉘는데...

1. **fast foward**  
   master, sub브랜치 하나씩 있다고 가정하고  
   sub에서 커밋발생, master는 변동없음. 근데 merge하면  
   sub브랜치를 그냥 master로 지칭하고 병합해버림  
   ※ `다 쓰고 필요없는 브랜치는 -d 로 없애버리면 된다`

2. **3-way merge**  
   일반적인 merge  
   master에서 커밋하고 merge하면 sub브랜치가  
   master로 병합되고 새로운버전으로 커밋된다

![merge](https://user-images.githubusercontent.com/81945553/168601450-84fa6d7d-f272-4afb-8ded-a8563599aa0c.png)

## **Git flow**

Git을 활용하여 협업하는 흐름, 브랜치활용전략  
git flow는 어느정도 정해진 브랜치이름 지정법칙이나 기본원칙 등이 있지만 정답이 있는게 아니다

협업을 할 때 내가 원격저장소에 push할 수 있는지 여부에따라  
github에서 제시하는 2가지 방법이 있다

- shared repository model
- fork & pull model

**첫번째**는 말그대로 원격저장소를 공유해서 협업하는 구조인데  
원격저장소 생성자가 함께할 팀원을 초대하고 팀원이 수락해서  
collabolator에 등록되어야 push권한을 얻는다

**두번째**는 collabolator에 등록되지않고 push권한이 없는 상태에서  
작업하고 PR(pull request)하는 구조  
상대의 오픈소스에 일방적으로 contribute할 때 쓰는 방식

`※ fork란 원본 프로젝트 원격저장소에 영향을 미치지않고 자신이 직접 관리할 수 있는 원본저장소의 사본이다`  
그래서 fork하게 되면,  
나의username/상대방 저장소 이름  
이렇게 가져와진다

※ 소스코드란 컴퓨터프로그램을 사람이 읽을 수 있는 프로그래밍 언어로 기술한 텍스트 파일을 말한다
