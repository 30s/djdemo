from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from djdemo.forms import RegistrationForm


@login_required
def profile(request):
    return HttpResponseRedirect('/dashboard/')
    return HttpResponse('hello world')


@login_required
def dashboard(request):
    return HttpResponse('dashboard %s' % request.user.username)


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.set_password(password)
            user.save()
            return HttpResponse('registration ok!')


    ctx = {}
    ctx.update(csrf(request))
    return render_to_response('registration/registration.html', ctx)
