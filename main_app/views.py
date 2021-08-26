from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Blog


# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def blogs_index(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', {'blogs': blogs})

def blogs_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render (request, 'blogs/detail.html', {'blog': blog})

class BlogCreate(CreateView):
    model = Blog
    fields = '__all__'
    success_url = '/blogs/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BlogUpdate(UpdateView):
    model = Blog
    fields = ['description', 'date']
    success_url = '/blogs/'

class BlogDelete(DeleteView):
    model = Blog
    success_url = '/blogs/'