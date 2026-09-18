from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'app2/vista1_app2')


def vista1_app2(request):
    return render(request, 'app2/vista1_app2')


def vista2_app2(request):
    return render(request, 'app2/vista2_app2')