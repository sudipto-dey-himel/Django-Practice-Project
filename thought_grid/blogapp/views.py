from django.shortcuts import render
from .models import Blog
from .forms import BlogForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Create your views here.


# homepage view

def home(request):
    return render(request, 'blogapp/index.html')



# blog list view (explore page)
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blogapp/explore.html', {'blogs' : blogs})


# create
def create(request):
    if request.method=='POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'form.html', {'form' : form})





# edit
def edit(request, blog_id):
    blog_id = None
    blog = get_object_or_404(Blog, pk=blog_id, user=request.user)
    if request.method=='POST':
        form = BlogForm(request.POST, request.FILES, instance=blog_id)
        if form.is_valid():
            blog = form.save(commit = False)
            blog.user = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form=BlogForm(instance=blog_id)
    return render(request, 'form.html', {'form' : form})





# delete
def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, user=request.user)
    if request.method=='POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'delete.html', {'blog':blog})




# user registration
def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('blog_list')
        else:
            form = UserRegistrationForm(request)
        return render(request, 'registration/register.html', {'form':form})





