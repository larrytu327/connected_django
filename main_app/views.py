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
    fields = ['name', 'topics']
    template_name = "messageboards_create.html"

    def form_valid(self, form):
        form.instance.user_profile = self.request.user.userprofile
        return super(MessageBoardsCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('messageboards_detail', kwargs={'pk': self.object.pk})

class MessageBoardsDetail(DetailView):
    model = MessageBoard
    template_name = "messageboards_detail.html"

class MessageBoardsUpdate(UpdateView):
    model = MessageBoard
    fields = ['name', 'topics']
    template_name = "messageboards_update.html"

    def get_success_url(self):
        return reverse('messageboards_detail', kwargs={'pk': self.object.pk})
    
class MessageBoardsDelete(DeleteView):
    model = MessageBoard
    template_name = "messageboards_delete_confirmation.html"
    success_url = "/messageboards/"

@method_decorator(login_required, name='dispatch')
class PostCreate(View):
    def post(self, request, pk):
        title = request.POST.get("title")
        content = request.POST.get("content")
        posting_user = request.user
        messageboard = MessageBoard.objects.get(pk=pk)
        Post.objects.create(title=title, content=content, posting_user=posting_user, messageboard=messageboard)
        return redirect('messageboards_detail', pk=pk)

@method_decorator(login_required, name='dispatch')
class SchoolClasses(TemplateView):
    template_name = "schoolclasses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.request.user.userprofile
        if user_profile is not None and user_profile.school_class is not None:
            context["schoolclasses"] = SchoolClass.objects.filter(users__in=[user_profile])
        return context
    
class SchoolClassesCreate(CreateView):
    model = SchoolClass
    fields = ['school', 'grade', 'school_type']
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

