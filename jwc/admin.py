from django.contrib import admin
from .models import Question as Q
from .models import Answer as A


# Register your models here.


#register my Question Model


#Question기능에 세부 기능을 추가해줄 클래스 작성
class QuestionAdmin(admin.ModelAdmin):
    search_fields=['subject']


#Question모델을 Admin에 등록 + 세부 기능 추가한 클래스
admin.site.register(Q,QuestionAdmin)

admin.site.register(A)







#django admin docs
#https://docs.djangoproject.com/en/3.0/ref/contrib/admin/