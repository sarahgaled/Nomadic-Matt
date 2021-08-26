from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blog


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blogs_index(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', {'blogs': blogs})

def blogs_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render (request, 'blogs/detail.html', {'blog': blog })

class BlogCreate(CreateView):
    model = Blog
    fields = '__all__'
    success_url = '/blogs/'

class BlogUpdate(UpdateView):
    model = Blog
    fields = ['description', 'date']

class BlogDelete(DeleteView):
    model = Blog
    success_url = '/blogs/'