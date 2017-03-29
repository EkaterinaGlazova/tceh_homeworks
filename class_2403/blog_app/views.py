from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse

from blog_app.forms import MyForm

# Create your views here.


class MyView(View):

    def get(self, request):
        form = MyForm()
        c = {'form': form}
        return render(request, 'blog_app/form.html', c)

    def post(self, request):
        messages_dict = []
        form = MyForm(data=request.POST)
        if form.is_valid():
            message = (request.POST.get('message'))
            messages_dict.append(message)
            return HttpResponse(messages_dict)
        else:
            messages.error(request, 'Validation failed')
        c = {'form': form}
        return render(request, 'blog_app/form.html', c)
