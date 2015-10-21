from django.shortcuts import render
from .models import Task, Tag
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import UserProfile
from motivatin.forms import TaskForm, TagForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
import json

# Create your views here.
class TaskList(ListView):
    model = Task
    
    queryset = Task.objects.all()
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskList, self).dispatch(*args, **kwargs)
    
    def get_queryset(self):
        curruser = UserProfile.objects.get(user=self.request.user)
        tasks = Task.objects.all().filter(user=curruser)
        self.queryset = tasks
        return tasks
        
    def get_context_data(self, **kwargs):
        context = super(TaskList, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context

class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
        
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskCreate, self).dispatch(*args, **kwargs)
        
    def form_valid(self, form):
        curruser = UserProfile.objects.get(user=self.request.user)
        form.instance.user = curruser
        form.save()
        return super(TaskCreate, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(TaskCreate, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context

class TagCreate(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('home')
    
class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskUpdate, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(TaskUpdate, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
        
class TaskDetail(DetailView):
    model = Task
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskDetail, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(TaskDetail, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context

#class Landing(TemplateView):
    #template_name = "motivatin/landing.html"
    
class Home(TemplateView):
    template_name = "motivatin/home.html"