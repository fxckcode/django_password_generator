from django.shortcuts import render
from random import choice

# Create your views here.
def generate_password(length=12, uppercase=True, special=True, numbers=True):
    characters = 'abcdefghijklmnopqrstvwxyz'
    if uppercase:
        characters += 'ABCDEFGHIJKLMNOPQRSTVWXY'
    if special:
        characters += '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    if numbers:
        characters += '1234567890'
    return ''.join(choice(characters) for _ in range(length))

def home(request):
    if request.method == 'POST':
        length = int(request.POST.get('length', 12))
        uppercase = 'uppercase' in request.POST
        special = 'special' in request.POST
        numbers = 'numbers' in request.POST
        password = generate_password(length, uppercase, special, numbers)
        return render(request, 'generator/home.html', {'password': password})
    else:
        return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')
