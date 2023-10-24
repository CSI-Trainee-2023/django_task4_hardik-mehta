import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class baseModel(models.Model):
    uid = models.UUIDField(default = uuid.uuid4, editable=False,primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    class Meta:
        abstract = True

class Question(baseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="questions")
    questions_text = models.CharField(max_length=100)

    def calculate_percentage(self):
        answer = self.answer.all()
        total_votes =0
        for answer in answer:
            total_votes += answer.counter

        payload = []
        for answer in  answer :
            payload.append(int((answer.counter / total_votes)* 100))

        return payload 

        #formula = C/V * 100

    def __str__(self) -> str:
        return self.questions_text


class Answer(baseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name="answer")
    answer_text = models.CharField(max_length=100)
    counter = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.answer_text    
