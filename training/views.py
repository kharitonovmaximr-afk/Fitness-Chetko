from django.shortcuts import render
from .models import exe
from django.db.models import Q


def equipment(request):
    return render(request, 'training/trenirovka-equipment.html')


def muscles(request):
    selected_equipment = request.GET.get('equipment', '')
    return render(request, 'training/trenirovka-muscles.html', {
        'selected_equipment': selected_equipment
    })


def exercises(request):
    selected_equipment = request.GET.get('equipment', '')
    selected_muscles = request.GET.get('muscles', '')

    # Начинаем с полного списка
    exercises_qs = exe.objects.all()

    # Фильтрация по инвентарю
    if selected_equipment:
        equipment_list = [eq.strip() for eq in selected_equipment.split(',') if eq.strip()]
        # Используем Q для фильтрации по нескольким значениям
        eq_query = Q()
        for equipment in equipment_list:
            eq_query |= Q(inventory__icontains=equipment)
        exercises_qs = exercises_qs.filter(eq_query)

    # Фильтрация по мышцам
    if selected_muscles:
        muscles_list = [muscle.strip() for muscle in selected_muscles.split(',') if muscle.strip()]
        mus_query = Q()
        for muscle in muscles_list:
            mus_query |= Q(muscles__icontains=muscle)
        exercises_qs = exercises_qs.filter(mus_query)

    # Убираем дубли (если одно упражнение подходит под несколько условий)
    exercises_qs = exercises_qs.distinct()

    return render(request, 'training/trenirovka-exercises.html', {
        'exercise': exercises_qs,
        'selected_equipment': selected_equipment,
        'selected_muscles': selected_muscles
    })



def saving(request):
    selected_equipment = request.GET.get('equipment', '')
    selected_muscles = request.GET.get('muscles', '')

    # Фильтрация тех же упражнений, что и на предыдущей странице
    exercises_qs = exe.objects.all()

    if selected_equipment:
        equipment_list = [eq.strip() for eq in selected_equipment.split(',') if eq.strip()]
        eq_query = Q()
        for eq in equipment_list:
            eq_query |= Q(inventory__icontains=eq)
        exercises_qs = exercises_qs.filter(eq_query)

    if selected_muscles:
        muscles_list = [mus.strip() for mus in selected_muscles.split(',') if mus.strip()]
        mus_query = Q()
        for mus in muscles_list:
            mus_query |= Q(muscles__icontains=mus)
        exercises_qs = exercises_qs.filter(mus_query)

    exercises_qs = exercises_qs.distinct()

    return render(request, 'training/trenirovka-saving.html', {
        'exercise': exercises_qs,
        'selected_equipment': selected_equipment,
        'selected_muscles': selected_muscles
    })