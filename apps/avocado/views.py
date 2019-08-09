from django.shortcuts import render, redirect
from django.utils.crypto  import get_random_string



def index(request):
    word = get_random_string(length=14)
    if 'counter' not in request.session:
        request.session['counter'] = 1
        request.session['counter'] += 1
    context = {
        'word' : word
    }    
    return render(request,'avocado/index.html', context)

def generate(request):
    return redirect('/')

def reset(request):
    request.session['counter'] = 0
    return redirect('/')
