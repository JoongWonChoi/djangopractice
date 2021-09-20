from django.urls import path
from . import views
import jwc


app_name  = 'jwc'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('<int:q_id>/', views.detail, name='detail'),
    path('answer/create/<int:q_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create')

]
