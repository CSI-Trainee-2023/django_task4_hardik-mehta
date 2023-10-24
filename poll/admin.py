from django.contrib import admin

# Register your models here.
from .models import Question , Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["questions_text" , "user" ]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["answer_text" ,"questions_text", "counter" ]


    def questions_text(self , obj):
        return obj.question.questions_text