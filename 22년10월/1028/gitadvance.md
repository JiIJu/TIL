# git advanced

## git undoing
작업 되돌리기
* working directory 작업단계
*  staging area 작업단계
* repository 작업단계


## woking directory 작업단계
* working directory에서 수정한 파일 내용을 이전 커밋상태로 되돌리기
* git restore

## staging Area 작업단계
* staging Area에 반영된 파일을 working Directory로 되돌리기
* **git rm --cached**
* **git restore --staged**

## repository 작업단계
* 커밋 완료한 파일을 staging area로 되돌리기
* **git commit --amend**


## working Directory 작업단계 되돌리기
*git restore*

working Directory에서 수정한 파일을 수정전(직전커밋)으로 되돌리기
이미 버전 관리가 되고있는 파일만 되돌리기 가능
git restore를 통해 되돌리면 해당 내용을 복원할 수 없음

**git restore {파일이름}**

1. git init 명령어로 초기화
2. 변경후 커밋
3. 

## staging Area작업단계 되돌리기
staging area에 반영된 파일을 working directory로 되돌리기
root-commit 여부에 따라 두가지 명령어로 나뉨
* root-commit이 없는경우 : git rm --cached
* root-commit이 있는경우 : git restore --staged

## **git rm --cached**
1. git저장소 초기화
2. test.md 파일생성후 add
3. git rm --cached를 사용해서 staging area

## **git restore --staged**
root-commit 이 있는 경우 사용

**git restore --staged {파일이름}**


## Repository 작업단계 되돌리기
**git commit --amend**
* 커밋을 완료한 파일을 staging Area로 되돌리기
상황별로 두가지 기능으로 나뉨

* staging area에 올라온 내용이 없다면 직전 커밋의 메세지만 수정

* staging area에 새로 올라온 내용이 있다면 직전 커밋을 덮어쓰기

* **이전 커밋을 완전히 고쳐서 새커밋으로 변경하므로 이전커밋은 일어나지 않은 일이되며 히스토리에도 남지않음을 주의**

**현재 commit된 메세지 확인하기 : git reflog**
## vim 간단사용법
* 입력모드 (i) : 문서편집기능
* 명령모드 (esc) : 저장및 종료 (:wq)

## Git reset
프로젝트를 특정 커밋상태로 되돌림

특정 커밋으로 되돌아 갔을 때 해당 커밋 이후로 쌓았던 커밋들은 저눕 사라짐

* **git reset [옵션] {커밋 ID}**
* 옵션은 soft,mixed,hard 중 하나를 작성
* 커밋 id는 되돌아가고 싶은 시점의 커밋 ID를 작성

## **--soft**
#### * 해당 커밋으로 되돌아가고 되돌아간 커밋 이후의 파일은 Staging Area로 되돌려놓음

##  **--mixed**
#### *  해당 커밋으로 되돌아가고 되돌아간 커밋이후의 파일들은 working directory로 되돌려놓음
#### *  git reset옵션의 기본값

##  **--hard**
####  * 해당 커밋으로 되돌아가고 되돌아간 커밋 이후의 파일들은 working directory에서 삭제 ==> 따라서 사용에 주의
####  * 기존의 untracked파일은 사라지지않고 Untracked로 남아있음


## git reflog
* git reflog명령어를 이용하면 reset하기전의 과거 커밋내역을 모두 조회 가능
* git reset 의 hard 옵션은 working directory 내용까지 삭제하므로 위험할 수 있음
*  이후 해당 커밋으로  reset하면 hard 옵션으로 삭제된 파일도 복구가능

## Git revert
 * 과거를 없었던 일로 만드는 행위로 이전 커밋을 취소한다는 새로운 커밋을 생성함.
 * **git revert {커밋ID}**
 * 커밋 ID는 취소하고 싶은 커밋 ID를 작성

 ## git reset과 차이점
 * 개념적 차이
 
 reset 은 커밋내역을 삭제하는반면 revert는 새로운 커밋을 생성함

 revert는 github를 통해 협업할 때 커밋내역의 차이로 인한 충돌방지

 * 문법적 차이

 git reset ~라고 작성하면 ~라는 커밋으로 되돌아간다는 뜻

 git revert ~라고 작성하면 ~라는 커밋 한개를 취소한다는 뜻
 (~~라는 커밋이 취소되었다는 새로운 커밋을 생성)

## Git branch
작업공간을 여러갈래로 나누어 독립적으로 작업할 수 있도록 도와주는 git 도구

###  장점
1. 브랜치는 독립공간을 형성하기 때문에 원본(master)에 대해 안전함
2. 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능
3. git은 브랜치를 만드는 속도가 굉장히 빠르고 적은용량을 소모함

## 조회

- git branch : 로컬 저장소의 브랜치 목록 확인

- git branch -r : 원격 저장소의 브랜치목록 확인
## 생성
- git branch {브랜치 이름} : 새로운 브랜치 생성

- git branch {브랜치 이름}{커밋 ID}
## 삭제

- git branch -d {브랜치이름} : 병합된 브랜치만 삭제가능
 
- git branch -D {브랜치이름} : 강제삭제

 
## Git switch

- git switch {브랜치이름} : 다른브랜치로 이동

- git switch -c {브랜치이름} : 브랜치를 새로 생성 및 이동

- git switch -c {브랜치이름} {커밋 ID} : 특정 커밋기준으로 브랜치 생성 및 이동

- ### **switch 하기전에 해당 브랜치의 변경사항을 반드시 커밋 해야함을 주의**
- ### 다른 브랜치에서 파일을 만들고 커밋하지않은 상태에서 switch를 하면 브랜치를 이동했음에도 불구하고 해당파일이 그대로 남아있게 됨.

## HEAD

HEAD는 현재 브랜치를 가리키고 각 브랜치는 자신의 최신 커밋을 가리키므로 결국 HEAD가 현재 브랜치의 최신 커밋을 가리킨다고 할 수 있음.

Git log  혹은 cat .git/HEAD 를 통해 현재 HEAD가 어떤 브랜치인지 알 수 있음.

## Git merge

분기된 브랜치들을 하나로 합치는 명령어

master 브랜치가 상용이므로 주로 master 브랜치에 병함

**git nerge {합칠 브랜치 이름}**

*  병합하기 전에 브랜치를 합치려고 하는 즉 브랜치로 switch 해야함
* 병합에는 세종류가 존재
  1. fast-forword
  2. 3-way Merge
  3. Merge Conflict

## Fast-Forword
- 마치 빨리감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법
(master) $ git merge hotfix

## 3-way Merge
- 각 브랜치의 커밋 두개와 공통 조상 하나를 사용하여 병합하는 방법
(master) $ git merge hotfix

## Merge Conflict
- 두 브랜치에서 같은 부분을 수정한 경우 , git이 어느 브랜치의 내용으로 작성해야 하는지 판단하지 못하여 중돌이 발생했을 때 이를 해결하며 병합하는 방법
- 보통 같은 파일의 같은부분을 수정했을 때 자주 발생함

### **충돌은 언제 일오나는가?**
- 두 브랜치에서 서로 다른 파일을 수정 후 병합하는경우 => Merge

## Git workflow
- Branch와 원격 저장소를 이용해 협업을 하는 두가지 방법
  - 원격 저장소 소유권이 있는경우 : Shared repository model
  - 원격 저장소 소유권 없는 경우 : fork & pull model

## shared repository model
- 원격 저장소가 자신의 소유이거나 collaborator 로 등록되어 있는 경우
- master 브랜치에 직접 개발하는것이 아니라 기능별로 브랜치를 따로 만들어 개발
- Pull Request를 사용하여 팀원간 변경 내용에 대한 소통 진행

## Fork & Pull model
- 오픈소스 프로젝트와 같이 , 자신의 소유가 아닌 원격 저장소인 경우
- 원본 원격 저장소를 그대로 내 원격 저장소에 복제(이러한 행위를 Fork라고함)
- 기능완성 후 복제한 내 원격 저장소에 Push
- 이후 Pull Request를 통해 원본 원격 저장소에 반영될 수 있도록 요청함

## Github - flow
- 복잡한 git flow를 개선하여 git hub에서 사용하는 방식