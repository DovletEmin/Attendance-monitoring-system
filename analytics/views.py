from rest_framework import viewsets
from .models import UserCreation
from .serializers import UserCreationSerializer
from django.shortcuts import render
from datetime import date, timedelta
from django.http import JsonResponse



class AttendanceRecordCreateSet(viewsets.ModelViewSet):
    queryset = UserCreation.objects.all()
    serializer_class = UserCreationSerializer


# def created_user_list(request):
#     records = UserCreation.objects.all()
#     return render(request, 'created_user_list.html', {'records': records})



def attendance_list(request):
    today = date.today()
    date_str = request.GET.get('date')
    selected_date = today  # По умолчанию — сегодня

    # Если есть дата в GET — используем её
    if date_str:
        try:
            selected_date = date.fromisoformat(date_str)
        except ValueError:
            selected_date = today

    # Фильтрация
    records = UserCreation.objects.filter(user_updated_date=selected_date)

    search_query = request.GET.get('search')
    if search_query:
        records = records.filter(user_name__icontains=search_query)

    return render(request, 'created_user_list.html', {
        'records': records,
        'selected_date': selected_date,
        'today': today,
        'search': search_query or '',
    })


def attendance_ajax(request):
    selected_date = request.GET.get('date')
    search_query = request.GET.get('search', '')

    try:
        selected_date = date.fromisoformat(selected_date)
    except (ValueError, TypeError):
        selected_date = date.today()

    records = UserCreation.objects.filter(user_updated_date=selected_date)

    if search_query:
        records = records.filter(user_name__icontains=search_query)

    data = [
        {
            'user_id': r.user_id,
            'user_name': r.user_name,
            'date': r.user_updated_date.strftime('%d-%m-%Y'),
            'time': r.user_updated_time.strftime('%H:%M'),
        }
        for r in records
    ]

    return JsonResponse({'records': data})