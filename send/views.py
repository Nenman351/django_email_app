from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView

from send.models import SendMail


# Create your views here.

def sendMail(request):
    send = SendMail.objects.all()
    context = {'send': send}
    return render(request, 'send/send.html', context)


def greet(request, pk):
    send = get_object_or_404(SendMail, pk=pk)
    return HttpResponse('Successful', {'send': send})


class SendListView(ListView):
    model = SendMail
    template_name = 'sendMail/send_list.html'
    context_object_name = 'sendMail'


class SendDetailView(DetailView):
    model = SendMail
    template_name = 'sendMail/send_detail.html'
    context_object_name = 'sendMail'


class SendCreateView(CreateView):
    model = SendMail
    template_name = 'sendMail/send_new.html'
    fields = ['subject', 'receiver', 'body', 'sender']
    success_url = reverse_lazy('home')


class SendUpdateView(UpdateView):
    model = SendMail
    template_name = 'sendMail/send_edit.html'
    fields = ['subject', 'body']


class SendDeleteView(DeleteView):
    model = SendMail
    template_name = 'sendMail/send_delete.html'
    success_url = reverse_lazy('home')
