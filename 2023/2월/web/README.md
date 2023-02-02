# C102_SUB_PJT1

## 팀명 : 개발집 막내 아들

## 그라운드 룰

1. 특이사항 공유하기
2. 점심 메뉴 공유하기
3. 연락 답장 잘하기
4. 회의 시, 1인 1의견 제시하기
5. 각종 이득 되는 정보 공유하기

## 마인드 셋

1. 항상 팀원을 존중하자
2. 1인분은 꼭 수행하기
3. 서로 부족한 점 채워주기
4. 건강관리 잘하기
5. 안 되면 될 때까지

## 가상환경설정

1. virtualenv env
2. source ./env/Scripts/activate
3. pip install --upgrade google-cloud-storage
   가상환경 빠져나오기 => deactivate

## 01/10 tts-test중

### 참고 블로그 주소 https://webnautes.tistory.com/1247

## 01/11

### STT 욕설감지 https://woochan-autobiography.tistory.com/881

### https://ehdrh789.tistory.com/29

1. 음성파일 녹음
2. 음성파일 stereo > mono 변환
3. 구글 클라우드에 파일 업로드
4. 구글 클라우드에 변환 후 업로드

- 구글 클라우드에 파일 업로드
  gsutil cp mono.wav gs://tts_file
- 구글 클라우드에 변환 후 업로드

## 업로드 공식문서 : https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running

gcloud ml speech recognize-long-running gs://tts_file/mono.wav --language-code=ko-KR --async --output-uri=gs://tts_file/output.json --filter-profanity

<!-- gcloud ml speech recognize-long-running gs://tts_file/mono.wav --language-code=ko-KR --async --output-uri=gs://tts_file/ --filter-profanity -->

--async => 진행 중인 작업이 완료될 때까지 기다리지 않고 즉시 반환합니다.
(--filter-profanity) => 욕설 필터링
파일실행
gcloud ml speech operations describe 3033708335622480475

json 저장
gcloud ml speech operations describe 8292352000618613254 > result.json

### google cloud sdk shell 사용법

https://puzzle-puzzle.tistory.com/entry/Qwiklabs-BasicsCloud-Storage%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EC%8A%A4%ED%86%A0%EB%A6%AC%EC%A7%80-using-Cloud-Shell

### 01.19 stt구현

송빈 > google cloud에 wav파일 업로드
이주 > GCP에서 파일 다운로드 후 wav파일 텍스트로 변환

할일 : 데이터셋 노가다
.

### 01.15

## text학습 https://wikidocs.net/24873


source venv/Scripts/activate

# 서버 키는법 python manage.py runserver 192.168.100.105:8000

conda list --export > packagelist.txt

conda install --file packagelist.txt