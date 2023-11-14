from django.shortcuts import render, redirect

from test_task_korteks_app.models import JobTitle, Employee


def main(request):
    return render(request, 'test_task_korteks_app/main.html')


def job_title_list(request):
    job_titles_list = JobTitle.objects.all()
    context = {
        'job_titles_list': job_titles_list
    }
    return render(request, 'test_task_korteks_app/job_title_list.html', context=context)


def job_title_detail(request, job_title_id):
    job_title = JobTitle.objects.get(id=job_title_id)
    context = {
        'job_title': job_title,
    }
    return render(request, 'test_task_korteks_app/job_title_detail.html', context=context)


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
            return redirect('test_task_korteks_app:job_title_detail', job_title_id=job_title_id)
    return render(request, 'test_task_korteks_app/job_title_change.html', context)


def job_title_delete(request, job_title_id):
    job_title = JobTitle.objects.get(id=job_title_id)
    job_title.delete()
    return redirect('test_task_korteks_app:job_titles_list')


def employees_list(request):
    employees = Employee.objects.all()
    context = {
        'employees_list': employees
    }
    return render(request, 'test_task_korteks_app/employee_list.html', context)


def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    context = {
        'employee': employee
    }
    return render(request, 'test_task_korteks_app/employee_detail.html', context=context)


def employee_add(request):
    job_titles = JobTitle.objects.values_list('name', flat=True)
    context = {
        'job_titles': job_titles
    }
    if request.method == 'POST':
        surname = request.POST['surname']
        firstname = request.POST['firstname']
        try:
            father_name = request.POST['father_name']
        except KeyError:
            father_name = None
        employment_date = request.POST['employment_date']
        try:
            job_title_name = request.POST['job_title']
            job_title = JobTitle.objects.get(name=job_title_name)
        except KeyError:
            job_title = None
        Employee.objects.create(
            surname=surname,
            firstname=firstname,
            father_name=father_name,
            employment_date=employment_date,
            job_title=job_title
        )
        context['message'] = 'Добавлен новый сотрудник'

    return render(request, 'test_task_korteks_app/employee_add.html', context=context)


def employee_change(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    job_titles = JobTitle.objects.values_list('name', flat=True)
    context = {
        'job_titles': job_titles,
        'employee': employee
    }

    if request.method == 'POST':
        surname = request.POST['surname']
        firstname = request.POST['firstname']
        try:
            father_name = request.POST['father_name']
        except KeyError:
            father_name = None
        employment_date = request.POST['employment_date']
        try:
            job_title_name = request.POST['job_title']
            job_title = JobTitle.objects.get(name=job_title_name)
        except KeyError:
            job_title = None
        employee.surname = surname
        employee.firstname = firstname
        employee.father_name = father_name
        employee.employment_date = employment_date
        employee.job_title = job_title
        employee.save()
        context['message'] = 'Изменено'

    return render(request, 'test_task_korteks_app/employee_change.html', context=context)


def employee_delete(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return redirect('test_task_korteks_app:employees_list')
