from django.shortcuts import render
from django.http import HttpResponse
from my_app_1.models import Worker

from .forms import AddWorkerForm


def index(request):
    context = {'greet': 'Hello World'}

    return render(request, 'index.html', context)


def workers(request):

    
    # change_worker = Worker.objects.get(id=3)
    # change_worker = Worker.objects.get(id=3).delete() <- удаляем запись полностью  
    # change_worker.second_name = 'Wood'
    # change_worker.save()

    all_workers = Worker.objects.all()

    # for worker in all_workers:
    #     workers_dict['name'] = worker.name
    #     workers_dict['second_name'] = worker.second_name
    #     workers_dict['salary'] = worker.salary
        
    #     workers_data.append(workers_dict)

    filtered_workers = Worker.objects.filter(name = 'Lavash')

    context =  {
        'workers_data': all_workers,
        'workers_salary': filtered_workers
        }

    return render(request, 'workers.html', context)


def add_worker(request):

    if request.method == 'POST':
        form = AddWorkerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            second_name = form.cleaned_data['second_name']
            salary = form.cleaned_data['salary']

            new_worker = Worker(name=name, second_name=second_name, salary=salary)

            new_worker.save()

            # Worker.objects.create(name=name, second_name=second_name, salary=salary)
        
        else:
            return HttpResponse('Ошибка при отправке формы')
    else:
        form = AddWorkerForm()
    context = {
        'form': form
    }

    return render(request, 'add_worker.html', context)