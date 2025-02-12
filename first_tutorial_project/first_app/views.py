from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello, world. You're at the <b>first_tutorial_project</b> index.</h1>") # This is the original line
    my_dict = {'my_variable': "Hello, I am from first_app/views.py!"}
    return render(request, 'index.html', context=my_dict)