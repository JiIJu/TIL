from django.shortcuts import render, redirect , get_list_or_404, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Record
# from .models import Record
from .forms import RecordForm

import datetime

from django.http import StreamingHttpResponse
import os
from record.models import Image
from .video import VideoCamera

# Create your views here.


# webcam 재생함수
cam = VideoCamera()


# 임시 페이지
def index(request):
    return render(request, 'record/index.html')



#에러 페이지
def page404(request):
    return render(request, 'record/page404.html')
check=0
def test(request):
    global check
    check+=1
    context = {
        'check' : check,
    }
    return render(request,'record/test.html',context)

#삭제
@login_required
def delete(request, pk):
    record = get_object_or_404(Record,pk=pk)
    if record.user==request.user:    
        record.delete()
        return redirect('record:totalrecord')
    else:
        return redirect('record:page404')



# 메인페이지 로그인후 진입
@login_required
def main(request):
    return render(request, 'record/main.html')



# 홈페이지 (로그인, 회원가입)
def home(request):
    return render(request, 'record/home.html')



# 날짜별 기록 차트
@login_required
def chart(request):
    return render(request, 'record/chart.html')



# 전체 운동 기록
@login_required
def totalrecord(request):
    records = Record.objects.all()
    context = {
        'records': records,
    }
    return render(request, 'record/totalrecord.html', context)



# 기록 수동저장
@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect('record:main')
    else:
        form = RecordForm()
    context = {
        'form': form,
    }
    return render(request, 'record/create.html', context)



# json 확인용
def jsonrecord(request):
    records = list(Record.objects.all().values())
    for i in records:
        print(i['exercise'])
    context = {
        'records' : records,
    }
    return JsonResponse(context)



directory = os.getcwd()
filePath = directory + '/record/static/record/img/'
good, bad = 0, 0



# 실시간 운동영상
def live(request):
    global good,bad
    # ans = cam.get_ans()
    ans=1
    if ans == 0:
        good +=1
    else:
        bad +=1
    
    context = {
        'ans': ans,
        'good':good,
        'bad':bad,
    }
    return render(request, 'record/live.html', context)
# cam.get_msg()

def gen(camera):
	while True:
		frame = cam.get_frame()
		yield(b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def stream2(request):
    try:
        return StreamingHttpResponse(gen(()), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass


# # 지울지말지 테스트해야됨
# def playback(request):
# 	image_list = Image.objects.all()
# 	return render(request, 'record/playback.html',
# 							{'image_list' : image_list})
# def playback_show(request, select_image):
# 	image_list = Image.objects.all()
# 	return render(request, 'record/playback.html',
# 							{'image_list' : image_list,  'select_image' : select_image})
# def setting(request):
#  return render(request, 'record/setting.html')

 

@login_required
def deepcreate(request):

    a = { 
        'exercise' : '자동',
        'count' : 123,
        'time' : 123,
        'perfect' : 1223,
        'good' : 1253,
        'bad' : 1234,
    }
    Record(
        exercise = a['exercise'],
        count = a['count'],
        time = a['time'],
        date = datetime.datetime.now().date(),
        perfect = a['perfect'],
        good = a['good'],
        bad = a['bad'],
        user = request.user,
    ).save()

    return redirect('record:main')





# STT데이터 통신
# @login_required
# def test(request):
#     from google.cloud import storage

#     bucket_name = 'tts_file'    # 서비스 계정 생성한 bucket 이름 입력
#     source_blob_name = 'file.wav'    # GCP에 저장되어 있는 파일 명
#     destination_file_name = './file.wav' # 다운받을 파일을 저장할 경로("local/path/to/file")

#     storage_client = storage.Client()
#     bucket = storage_client.bucket(bucket_name)
#     blob = bucket.blob(source_blob_name)

#     blob.download_to_filename(destination_file_name)

#     import speech_recognition as sr

#     r = sr.Recognizer()
#     harvard = sr.AudioFile('file.wav')
#     with harvard as source:
#         audio = r.record(source)

#     data = []
#     try:
#         data.append(r.recognize_google(audio,language='ko-KR'))
#         context = {
#             'data' : data,
#         }
#     except:
#         context = {
#             'data' : 'empty',
#         }

#     '''
#     여기에 딥러닝??
#     맞으면 로봇에 신호보내기
#     '''
#     return render(request, 'record/test.html',context)

