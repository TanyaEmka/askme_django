from django.shortcuts import render
from app import models
from app import functions
from django.core.paginator import Paginator


# Create your views here.
def tag_questions(request, tag):
    full_tag = functions.get_tag_by_name(tag)
    context_questions = []
    if full_tag != {}:
        context_questions = functions.get_tag_questions(models.QUESTIONS, full_tag['id'])
    if full_tag == {}:
        full_tag = {'id': 0, 'name': tag}
    context = {'data': {
        'questions': functions.get_page_data(context_questions, 10, request.GET.get('page')),
        'tag': full_tag,
    }}
    return render(request, 'tag_questions.html', context)


def questions_page(request):
    context_questions = functions.get_page_data(models.QUESTIONS, 10, request.GET.get('page'))
    context = {'data': {
        'questions': context_questions,
    }}
    return render(request, 'index.html', context)


def new_question(request):
    return render(request, 'new_question.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')


def user_page(request):
    return render(request, 'user_page.html')


def question_page(request, question_id):
    context_question = {}
    context_user = {}
    context_answers = []
    for question in models.QUESTIONS:
        if question['id'] == question_id:
            context_question = question
    for user in models.USERS:
        if user['id'] == context_question['user']:
            context_user = user
    for answer in models.ANSWERS:
        if answer['question'] == question_id:
            context_answers.append(answer)

    context = {'data': {
        'question': context_question,
        'user': context_user,
        'answers': functions.get_page_data(context_answers, 5, request.GET.get('page')),
    }}
    return render(request, 'question_page.html', context)
