from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from index.models import CustomUserCreationForm, Post, PostForm


# Create your views here.
def start(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the new user to the database
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()  # Display an empty form for GET request
    return render(request, 'register.html', {'form': form})



@login_required
def home(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'homepage.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save yet
            post.author = request.user  # Set the author to the current logged-in user
            post.save()  # Now save the post
            return redirect('home')  # Redirect to a list or a success page
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})

# Edit Post view
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})

# Delete Post view
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('home')


# Search Posts
def search_posts(request):
    query = request.GET.get('q', '')
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()

    return render(request, 'homepage.html', {'posts': posts})