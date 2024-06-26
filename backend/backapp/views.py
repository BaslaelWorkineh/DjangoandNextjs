from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions, Choices
# Create your views here.
def index(request):
    latest_question_list = Questions.objects.order_by("-pub_date")[:5]
    result = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(result)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# Path: backend/backapp/urls.py
# Compare this snippet from backend/backapp/urls.py:
# """
