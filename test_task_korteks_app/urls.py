from django.urls import path
from . import views

app_name = 'test_task_korteks_app'
urlpatterns = [
    path('', views.main, name='main'),
    path('job_title/', views.job_title_list, name='job_titles_list'),
    path('job_title/<int:job_title_id>', views.job_title_detail, name='job_title_detail'),
    path('job_title/add/', views.job_title_add, name='job_title_add'),
    path('job_title/change/<int:job_title_id>', views.job_title_change, name='job_title_change'),
    path('job_title/delete/<int:job_title_id>', views.delete_job_title, name='delete_job_title'),
]
