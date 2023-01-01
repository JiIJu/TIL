from django import forms
from .models import Comment, Question

class QuestionForm(forms.ModelForm):
    issue_a = forms.CharField(label = "RED TEAM")
    issue_b = forms.CharField(label = "BLUE TEAM")

    class Meta:
        model = Question
        fields = '__all__'

class CommentForm(forms.ModelForm):
    # 선택을 위한 input이 체크박스(기본값)이 아니라 셀렉트로 바꾸고 싶을 때
    PICKS = [
        (False,"RED TEAM"),
        (True , "BLUE TEAM")
    ]

    # pick입력 정보는 select 형식으로 선택
    pick = forms.ChoiceField(choices=PICKS,widget=forms.Select())
    class Meta:
        model = Comment
        #사용자로부터 입력 받아야 하는 필드 설정
        fields = ["pick","content"]