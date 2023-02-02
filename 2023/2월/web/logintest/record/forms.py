from django import forms
from .models import Record

class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        # fields = ['excercise','count','time','perfect','good','bad','date']
        exclude = ('user',)