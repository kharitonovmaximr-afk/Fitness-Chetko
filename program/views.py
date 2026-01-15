from django.shortcuts import render

def programms(request):
    return render(request, 'program/program.html')
def exer(request):
    return render(request, 'program/program-exercises.html')


