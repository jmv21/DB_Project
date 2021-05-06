from django.shortcuts import render
from django.http import HttpResponse
from Monster_Hunter.models.Hunter import Hunter
from django.http import HttpResponse


# Create your views here.

def hunters(request):
    result =Hunter.objects.all()
    output = ', '.join([("Name: %s Rank: %i"%q.name %q.rank)  for q in result])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
