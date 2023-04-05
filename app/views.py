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
    paginator = Paginator(context_questions, 10)
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    context = {'data': {
        'questions': paginator.get_page(page_number),
        'tag': full_tag,
        'page': page_number,
    }}
    return render(request, 'tag_questions.html', context)


def questions_page(request):
    paginator = Paginator(models.QUESTIONS, 10)
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    context_questions = paginator.get_page(page_number)
    for i in range(len(context_questions)):
        if len(context_questions[i]['text']) > 75:
            context_questions[i]['text'] = context_questions[i]['text'][0:75] + '...'
    context = {'data': {
        'questions': context_questions,
        'page': page_number,
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

    paginator = Paginator(context_answers, 5)
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    context = {'data': {
        'question': context_question,
        'user': context_user,
        'answers': paginator.get_page(page_number),
        'page': page_number
    }}
    return render(request, 'question_page.html', context)
