from django.shortcuts import render

# Create your views here.

def condition(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'condition.html',d)

def loops(request):
    d={'name':'rahul'}
    return render(request,'loops.html',d)