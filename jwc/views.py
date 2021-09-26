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




#POST방식 : HTML body에 전송해야할 데이터를 담아서 전달. 
#서버에게 동일한 요청을 전달해도 항상 응답이 다를 수 있음. 서버의 상태나 데이터를 변경시킬 때 사용

#GET방식 : 서버로부터 정보를 전달하기 위한 메소드. 요청을 전송할 때 HTML body에 담지 않고 url 끝에 쿼리스트링을 통해 전달.
#쿼리스트링이란 ?와 함께 이름과 값으로 쌍을 이루는 방식. ?...com/jwc/name1=value&name2=valu2...


def question_create(request):
    '''
    jwc질문 등록

    '''
    #form 변수에 Questionform 연결
    #request 인자에 들어오는 값(POST / GET)에 따라 구분
    if request.method == "POST":
        #응답 method가 POST방식이면 Questionform에 전달된 내용 및 데이터를 전달하여 form 변수에 저장
        #즉 사용자가 작성한 'subject'와 'content' 의 내용이 전달되어 form에 저장되어 객체로 생성
        #forms.py 의 Questionform 클래스에서 Question model의 subject와 content 를사용할 필드로 상속시켰기 때문
        form = Questionform(request.POST)
        #만약 입력에 있어서 유효하지 않다면, 즉 지정한 속서인 subject나 content 둘 중 하나라도 작성하지 않는다면 작동하지 않음
        if form.is_valid():
            #.save(commit=False) : save 함수의 선택적 인수로 commit = True와 False 사용 가능
            #False를 사용하면 DB에 즉시 저장 x, DB에 데이터를 저장하기 전에 특정 행위를 하고 싶을 때 사용
            question = form.save(commit=False)
            #이 때 임시저장 즉 commit=False를 하지 않으면 오류 발생. Question 모델의 속성인  create_date가 정의되지 않았기 때문
            #question = form.save()
            question.create_date = timezone.now()
            question.save()
            return redirect("jwc:index")
    else:
        form = Questionform()
    context = {'form':form}
    return render(request, 'jwc/question_form.html', context)


#html template 문법 사용
#https://wikidocs.net/70736