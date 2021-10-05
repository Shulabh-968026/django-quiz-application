from django.http.response import JsonResponse
from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Course,Questions
from django.core.paginator import Paginator
def index(request):
    courses=get_list_or_404(Course)
    context={
        "courses":courses
    }
    return render(request,'myapp/course.html',context=context)


def questions(request,pk):
    question_list=Questions.objects.filter(quiz__id=pk)
    questions_all=[]
    total_question=0
    for question in question_list:
        questions=[]
        total_question +=1
        question_text=question.qusestion_text
        answer=question.answer
        option1=question.option1
        option2=question.option2
        options=[option1,option2]
        option3=question.option3
        if len(option3):
            options.append(option3)
        option4=question.option4
        if len(option4):
            options.append(option4)
        questions.append(total_question)
        questions.append(question_text)
        questions.append(answer)
        questions.append(options)
        questions_all.append(questions)
    paginator=Paginator(questions_all,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'myapp/questions.html',{"page_obj":page_obj})