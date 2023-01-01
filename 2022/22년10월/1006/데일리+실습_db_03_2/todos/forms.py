from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        # 1:N 관계 author는 우리가 입력할 필요가 없다.
        # fields = '__all__'
        exclude = ('author',)