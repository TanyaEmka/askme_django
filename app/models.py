from django.db import models

# Create your models here.
TAGS = [
    {'id': 1, 'name': 'django'},
    {'id': 2, 'name': 'python'},
    {'id': 3, 'name': 'HTML'},
]

QUESTIONS = [
    {'id': i + 1,
     'title': 'Как создать приложение? ' + str(i + 1),
     'text': 'Мой вопрос заключается в том, что мне необходимо сделать кое-что интересное. '
             'Я думаю над тем, как создать собственное веб-приложение. Не могли бы вы'
             'посоветовать, какие технологии мне нужно изучить и с каких языков '
             'программирования начать?',
     'answers': 10,
     'likes': 5,
     'tags': [TAGS[0], TAGS[1], TAGS[2]],
     'user': 1,
     'date': 'DD.MM.YYYY HH:MM'} for i in range(15)
]

USERS = [
    {'id': i + 1,
     'login': 'userxxx',
     'email': 'user2000@mail.ru',
     'password': '12345',
     'avatar': 'file.txt',
     'firstname': 'Firstname',
     'lastname': 'Lastname'} for i in range(3)
]

ANSWERS = [
    {'id': i + 1,
     'text': 'Во-первых, тебе необходимо начать изучать этот фраемворк, а также изучить данную технологию. '
             'Тебе будет легко сделать шаблонный пример, но над чем-то своим тебе придётся долго и упорно '
             'работать. Желаю удачи!',
     'likes': 5,
     'user': 2,
     'best_answer': 0,
     'question': 1,
     'date': 'DD.MM.YYYY HH:MM'} for i in range(13)
]

COOKIES = [
    {'user': '1'}
]