from django.shortcuts import render
from .models import Blog

# Create your views here.

def home(request):
    return render(request, 'blogapp/index.html')



def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blogapp/explore.html', {'blogs' : blogs})