from django.urls import path, include
from rest_framework.routers import DefaultRouter
from analytics.views import AttendanceRecordCreateSet
from analytics import views
from django.contrib import admin
from django.urls import path, include

router = DefaultRouter()
router.register(r'attendance', AttendanceRecordCreateSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.attendance_list, name='created_user_list'),
    path('attendance/ajax/', views.attendance_ajax, name='attendance_ajax'),
    
]
