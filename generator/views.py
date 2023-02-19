from django.shortcuts import render
from random import choice

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    characters = list('abcdefghijklmnopqrstvwxyz')
    generated_password = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTVWXY'))
    if request.GET.get('special'):
        characters.extend(list('!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    for x in range(length):
        generated_password += choice(characters)


    return render(request, 'generator/password.html', {'password': generated_password})