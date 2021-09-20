from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Question as Q
from .models import Answer as A
from .forms import Questionform

# Create your views here.

def home(request):
    return render(request,'jwc/home.html')


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
    answer = A.objects.get(id=q_id)
    context = {'q':question, 'a':answer}
    return render(request,'jwc/question_detail.html',context)

def answer_create(request, q_id):
    '''
    jwc 질문 답변 등록

    '''
    question = get_object_or_404(Q,pk = q_id)
    #질문에 대한 답변 목록(answer_set) 생성(.create)
    #what is answer_set? auto created?
    #https://pybo.kr/pybo/question/detail/83/?page=1
    #django automatically created 'modelname(in small alphabet)+ _set' if connected with foreign key
    question.answer_set.create(content=request.POST.get('content'),create_date = timezone.now())

    #redirect : url 매핑
    #render : template 매핑
    return redirect('jwc:detail', q_id = q_id)

def question_create(request):
    '''
    jwc질문 등록

    '''
    #form 변수에 Questionform 연결
    if request.method == "POST":
        form = Questionform(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect("jwc:index")
    else:
        form = Questionform()
    context = {'form':form}
    return render(request, 'jwc/question_form.html', context)


#html template 문법 사용
#https://wikidocs.net/70736