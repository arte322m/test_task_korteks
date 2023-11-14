from django.urls import path
from . import views

app_name = 'test_task_korteks_app'
urlpatterns = [
    path('', views.main, name='main'),

    path('job_title/', views.job_title_list, name='job_titles_list'),
    path('job_title/<int:job_title_id>/', views.job_title_detail, name='job_title_detail'),
    path('job_title/add/', views.job_title_add, name='job_title_add'),
    path('job_title/change/<int:job_title_id>/', views.job_title_change, name='job_title_change'),
    path('job_title/delete/<int:job_title_id>/', views.job_title_delete, name='job_title_delete'),

    path('employee/', views.employees_list, name='employees_list'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('employee/add/', views.employee_add, name='employee_add'),
    path('employee/change/<int:employee_id>/', views.employee_change, name='employee_change'),
    path('employee/delete/<int:employee_id>/', views.employee_delete, name='employee_delete'),
]
