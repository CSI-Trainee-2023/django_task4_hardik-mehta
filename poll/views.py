from tkinter.messagebox import QUESTION
from django.shortcuts import redirect, render
from poll.admin import QuestionAdmin

from poll.models import Question

# Create your views here.
def question_detail(request , question_uid):
    try:
        question_obj = Question.objects.get(uid = question_uid)
        context = {'question' : question_obj}
        return render(request,'question.html',context)
    
    except Exception as e :
        print(e)
        #return redirect('/')