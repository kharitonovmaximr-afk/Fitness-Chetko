from django.shortcuts import render
from .models import GTONormativ

def goal(request):
    return render(request, 'gto/gto-goal.html')


def normativy(request):
    gender = request.GET.get('gender', 'male')
    medal = request.GET.get('medal', 'bronze')
    age = request.GET.get('age')

    normativy = GTONormativ.objects.filter(gender=gender, medal=medal)

    # Определяем возрастную группу (пример — настрой под свои данные)
    if age:
        age = int(age)
        if 6 <= age <= 8:
            age_group = "6-8"
        elif 9 <= age <= 10:
            age_group = "9-10"
        elif 11 <= age <= 12:
            age_group = "11-12"
        elif 13 <= age <= 15:
            age_group = "13-15"
        elif 16 <= age <= 17:
            age_group = "16-17"
        elif 18 <= age <= 24:
            age_group = "18-24"
        elif 25 <= age <= 29:
            age_group = "25-29"
        elif 30 <= age <= 39:
            age_group = "30-39"
        elif 40 <= age <= 49:
            age_group = "40-49"
        else:
            age_group = "50+"

        normativy = normativy.filter(age_group=age_group)

    return render(request, 'gto/gto-normativy.html', {
        'normativy': normativy,
        'selected_gender': gender,
        'selected_medal': medal,
        'selected_age': age,
    })