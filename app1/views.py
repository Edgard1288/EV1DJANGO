from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'app1/vista1_app1')


def vista1_app1(request):
    return render(request, 'app1/vista1_app1')


def vista2_app1(request):
    return render(request, 'app1/vista2_app1')