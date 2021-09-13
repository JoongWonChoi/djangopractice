from django.shortcuts import render
from django.http import HttpResponse
from .models import Question as Q


# Create your views here.

def index(request):
    '''
    jwc 질문 목록 출력

    '''
    #질문 목록 출력 순서
    #기준이 되는 속성에 '-'를 붙이면 역순
    question_list = Q.objects.order_by('-create_date')
    context = {'question_list':question_list}

    return render(request, 'jwc/question_list.html',context)

def detail(request, q_id):
    '''
    jwc 질문의 답변 상세 페이지

    '''
    question = Q.objects.get(id=q_id)
    context = {'q':question}
    return render(request,'jwc/question_detail.html',context)


#html template 문법 사용
#https://wikidocs.net/70736