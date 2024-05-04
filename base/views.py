from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, "index.html", {"posts": posts})

#Auth
def registerUser(request):
    context ={}
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()

            login(request, user)
            return redirect('home')
    return render(request, "signup.html", context)


def loginUser(request):
    context ={}
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else: 
            context = {"message": "Invalid username or password"}
    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    return redirect("home")



#Post Crud
def about(request):
    return render(request, "about.html")


def contacts(request):
    return render(request, "contacts.html")

def getPost(request, pk):
    post =Post.objects.get(id=pk)
    return render(request, "post_detail.html",  {"post": post })

@login_required
def deletePost(request, pk):
    context ={}
    try:
        post = Post.objects.get(id=pk)
        # Check if the logged-in user is the author of the post
        if request.user == post.author:
            post.delete()
            return redirect("home")
        else:
            return HttpResponse("You are not authorized to delete this post.")
    except Post.DoesNotExist:
        return HttpResponse("Post does not exist.")
    
def createPost(request):
    context ={}
    if request.method == "POST":
        try:
            Post.objects.create(
                title = request.POST.get("title"),
                body = request.POST.get("description"),
                author = request.user
            )
            return redirect("home")
        except:
            context["message"] = "*Invalid Details"

    return render(request,"new_post.html", context)

def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.body = request.POST.get('description')
        post.save()
        return redirect("home")
    return render(request, "post_updated.html", context)
 