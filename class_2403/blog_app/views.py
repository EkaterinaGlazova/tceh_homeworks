from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse

from blog_app.forms import MyForm
from blog_app.models import Message
import json

# Create your views here.



class MyView(View):

    def get(self, request):
        form = MyForm()
        c = {'form': form}
        return render(request, 'blog_app/form.html', c)

    def post(self, request):
        form = MyForm(data=request.POST)
        if form.is_valid():
            message = form.save()
            new_message = json.dumps(message)
            return HttpResponse(new_message)
        else:
            messages.error(request, 'Validation failed')
        c = {'form': form}
        return render(request, 'blog_app/form.html', c)

class MessagesView(View):

    def get(self, request):
        all_messages = Message.objects.all()
        return render(request, 'blog_app/messages.html', {'all_messages': all_messages})

