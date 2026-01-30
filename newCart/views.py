from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Category, Blog
def home(request):
    # categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True).order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False,status = 'Published')

    context = {
       # 'categories': categories,
        'featured_post': featured_post,
        'post':posts,
    }
    return render(request, 'home.html', context)