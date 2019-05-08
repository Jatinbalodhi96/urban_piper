from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout


from .models import Task


def logout_view(request):
    logout(request)
    return HttpResponse('Logout successfully.')


def login_view(request):
    return render(request, 'login.html', {})


@login_required(login_url='/login', redirect_field_name='')
def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'username': request.user.username}
    return render(request, 'index.html', context)


def createTask(request):
    return HttpResponse(200)