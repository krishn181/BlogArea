from django.shortcuts import redirect, render
from assignment.models import About
from blogs.models import Blog
from newCart.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth



def home(request):
    all_posts = Blog.objects.filter(status='Published').order_by('-updated_at')

    hero_post = all_posts[:1]        # 1 before featured
    featured_post = all_posts[2:4]   # next 2 featured
    posts = all_posts[4:]            # rest recent posts
    #fetch about us
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'hero_post': hero_post,
        'featured_post': featured_post,
        'posts': posts,
        'about':about,
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('register')
        
    else:
        form = RegistrationForm()

    context={
        'form':form,
    }  
    return render(request, 'register.html', context)


def login(request):
    if request.method =="POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password = password)
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')
        

    form = AuthenticationForm()
    context={
        'form':form,
    }
    return render(request,'login.html',context)


def logout(request):
    auth.logout(request)
    return redirect('home')