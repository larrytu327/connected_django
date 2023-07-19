from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse 
from .models import MessageBoard, Post, SchoolClass
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"

class MessageBoards(TemplateView):
    template_name = "messageboards.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = self.request.GET.get("subject")
        if subject != None:
            context["messageboards"] = MessageBoard.objects.filter(subject__icontains=subject)

        else:
            context["messageboards"] = MessageBoard.objects.all()
        return context

class MessageBoardsCreate(CreateView):
    model = MessageBoard
    fields = ['name', 'topics', 'date_added', 'school_class']
    template_name = "messageboards_create.html"

    def get_success_url(self):
        return reverse('messageboards_detail', kwargs={'pk': self.object.pk})

class MessageBoardsDetail(DetailView):
    model = MessageBoard
    template_name = "messageboards_detail.html"

class MessageBoardsUpdate(UpdateView):
    model = MessageBoard
    fields = ['name', 'topics', 'date_added', 'school_class']
    template_name = "messageboards_update.html"

    def get_success_url(self):
        return reverse('messageboards_detail', kwargs={'pk': self.object.pk})
    
class MessageBoardsDelete(DeleteView):
    model = MessageBoard
    template_name = "messageboards_delete_confirmation.html"
    success_url = "/messageboards/"

class PostCreate(View):
    def post(self, request, pk):
        title = request.POST.get("title")
        content = request.POST.get("content")
        messageboard = MessageBoard.objects.get(pk=pk)
        Post.objects.create(title=title, content=content, messageboard=messageboard)
        return redirect('messageboards_detail', pk=pk)

class Login(TemplateView):
    template_name = "login.html"

class SchoolClasses(TemplateView):
    template_name = "schoolclasses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school = self.request.GET.get("school")
        if school != None:
            context["schoolclasses"] = SchoolClass.objects.filter(school__icontains=school)

        else:
            context["schoolclasses"] = SchoolClass.objects.all()
        return context
    
class SchoolClassesCreate(CreateView):
    model = SchoolClass
    fields = ['school', 'grades', 'school_type']
    template_name = "schoolclasses_create.html"

    def get_success_url(self):
        return reverse('schoolclasses_detail', kwargs={'pk': self.object.pk})
    
class SchoolClassesDetail(DetailView):
    model = SchoolClass
    template_name = "schoolclasses_detail.html"