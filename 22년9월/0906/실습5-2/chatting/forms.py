from django import forms
from .models import Chatting


class ChattingForm(forms.ModelForm):
    user = forms.CharField(
        label='작성자',
        widget=forms.TextInput(
            attrs={
                'class': 'my-user form-control',
                'placeholder': 'Nickname',
                'maxlength': 10,
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': 'Chat!',
                'rows': 5,
                'cols': 50,
            }
        )
        # error_messages={
        #     'required': '내용 입력하라고..',
        # }
    )

    class Meta:
        model = Chatting
        fields = '__all__'
