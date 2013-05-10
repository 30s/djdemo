from django.shortcuts import render_to_response

from djdemo.models import DictKey


def profile(request):
    ctx = {'keys': DictKey.objects.all()}
    return render_to_response('xpg_qa.html', ctx)
