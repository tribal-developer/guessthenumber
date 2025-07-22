from django.shortcuts import render
import random

def home(request):
    lucky_number = random.randint(0, 99)
    context = {'lucky_number': lucky_number}
    return render(request, 'index.html', context)