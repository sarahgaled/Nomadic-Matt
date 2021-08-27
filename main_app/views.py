from os import error
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'sj-travel-blog'

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def blogs_index(request):
    blogs = Blog.objects.filter(user=request.user)
    return render(request, 'blogs/index.html', {'blogs': blogs})

@login_required
def blogs_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render (request, 'blogs/detail.html', {'blog': blog})

class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    fields = '__all__'
    success_url = '/blogs/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ['description', 'date']
    success_url = '/blogs/'

class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = '/blogs/'

def add_photo(request, blog_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, blog_id=blog_id)
            blog_photo = Photo.objects.filter(blog_id=blog_id)
            if blog_photo.first():
                blog_photo.first().delete()
            photo.save()
        except Exception as err:
            print('An error occurred uploading file to S3: %s' % err)
    return redirect('blogs_detail', blog_id=blog_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blogs_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    