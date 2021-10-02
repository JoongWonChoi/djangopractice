from django.db import models

# Create your models here.


#모델 : class단위
#django에서 지원하는 속성 Field 모음
#https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types
#모델이 새로 생성되면 migration 새로 해줘야함

class Question(models.Model):
    #제목처럼 글자수 제한 가능한 항목 : Charfield
    subject = models.CharField(max_length=200)
    #내용처럼 글자수 제한이 힘든 항목 : TextField
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    #ForeignKey : 기존 모델을 속성으로 연결
    #on_delete=models.CASCADE : 이 속성에 연결된 속성이 삭제되면 같이 삭제됨
    #foreign key 관련 내용 : https://jwccoding.tistory.com/24
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content