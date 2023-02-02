### 01/16

## 가상환경 설정

python -m venv ./venv
source venv/Scripts/activate

## install파일들 다운로드

pip install -r requirements.txt

## install 파일 requirement에 저장

pip freeze > requirements.txt

## 장고설치

pip install django

## 프로젝트생성

django-admin startproject firstpjt .

## 앱 생성

python manage.py startapp articles

## 서버싱행

python manage.py runserver

## 더미데이터 생성

python manage.py seed [app이름] --number=[데이터 수]

## accounts 설정

settings 수정

pjt의 url수정

## 토큰

"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6IndsZGx3bjEyQG5hdmVyLmNvbSIsImV4cCI6MTY3MzgzNTMyMiwiZW1haWwiOiJ3bGRsd24xMkBuYXZlci5jb20ifQ.MShBxUM7aX2toBaX-WkT6INLRQpEOECfT-DurLiTZLM"
