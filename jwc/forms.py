from django import forms
from django.forms import fields, widgets
from jwc.models import Question


#django에는 두가지 form존재
#일반form과 모델form
#모델form은 모델과 연결된 form으로 저장하면 연결된 모델의 데이터를 저장 가능
#모델form 내부에 Meta클래스 필수
#Meta 클래스에는 사용할 모델과 모델의 속성 기입

#Questionform은 ModelForm을 상속받음
class Questionform(forms.ModelForm):
    class Meta:
        model = Question #사용할 모델
        fields = ['subject', 'content'] #Question form에서 사용할 Question 모델의 속성들
        #지정한 속성들의 모양 지정
        widgets = {
            'subject' : forms.TextInput(attrs={'class':'form-control'}),
            'content' : forms.Textarea(attrs={'class':'form-control', 'rows':10})
        }
        #지정한 속성들의 naming
        labels = {
            'subject' : '제목',
            'content' : '내용'
        }


#djangp form 더 알아보기
#https://docs.djangoproject.com/en/3.0/topics/forms/
