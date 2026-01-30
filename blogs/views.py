from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Blog, Category
# Create your views here.
def post_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category_id=category_id)
    try:
        category= Category.objects.get(pk=category_id)
    except:
        #when category is more than the given category is will go to home page
        return redirect('home')
    context = {
        'posts':posts,
        'category':category,
    }
    return render(request,'posts_by_category.html',context)