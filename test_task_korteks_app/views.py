from django.shortcuts import render, redirect

from test_task_korteks_app.models import JobTitle


def main(request):
    return render(request, 'test_task_korteks_app/main.html')


def job_title_list(request):
    job_titles_list = JobTitle.objects.all()
    context = {
        'job_titles_list': job_titles_list
    }
    return render(request, 'test_task_korteks_app/job_title_list.html', context=context)


def job_title_add(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        try:
            JobTitle.objects.get(name=name)
            context['message'] = 'Такая должность уже существует'
        except JobTitle.DoesNotExist:
            JobTitle.objects.create(name=name)
            context['message'] = 'добавлено'

    return render(request, 'test_task_korteks_app/job_title_add.html', context=context)


def job_title_detail(request, job_title_id):
    job_title = JobTitle.objects.get(id=job_title_id)
    context = {
        'job_title': job_title,
    }
    return render(request, 'test_task_korteks_app/job_title_detail.html', context=context)


def job_title_change(request, job_title_id):
    job_title = JobTitle.objects.get(id=job_title_id)
    context = {
        'job_title': job_title
    }
    if request.method == 'POST':
        new_job_title_name = request.POST['new_job_title_name']
        if job_title.name == new_job_title_name:
            context['message'] = 'Изменений нет'
            return render(request, 'test_task_korteks_app/job_title_change.html', context)
        try:
            JobTitle.objects.get(name=new_job_title_name)
            context['message'] = 'Такая должность уже существует'
        except JobTitle.DoesNotExist:
            job_title.name = new_job_title_name
            job_title.save()
            return redirect('test_task_korteks_app:job_title_detail', job_title=new_job_title_name)
    return render(request, 'test_task_korteks_app/job_title_change.html', context)


def delete_job_title(request, job_title_id):
    job_title = JobTitle.objects.get(id=job_title_id)
    job_title.delete()
    return redirect('test_task_korteks_app:job_titles_list')
