from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse 
from .models import MessageBoard, Post, SchoolClass
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"

@method_decorator(login_required, name='dispatch')
class MessageBoards(TemplateView):
    template_name = "messageboards.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["messageboards"] = MessageBoard.objects.filter(name__icontains=name, user_profile=self.request.user.userprofile)

        else:
            context["messageboards"] = MessageBoard.objects.filter(user_profile=self.request.user.userprofile)
        return context

class MessageBoardsCreate(CreateView):
    model = MessageBoard
    fields = ['name', 'topics', 'date_added', 'school_class']
    template_name = "messageboards_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MessageBoardsCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
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

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("messageboards")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

