from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Blog, Category, Comment
from django.db.models import Q
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

def blogs(request, slug):
    single_blog = get_object_or_404(Blog,
                                     slug=slug, 
                                     status='Published')

    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST.get('comment')
        comment.save()
        return HttpResponseRedirect(request.path_info)
    #comments 
    comment = Comment.objects.filter(blog=single_blog)
    comment_cnt = comment.count()
    context={
        'single_blog':single_blog,
        'comment':comment,
        'comment_cnt': comment_cnt,
    }
    return render(request,'blogs.html',context)


def search(request):
    keyword = request.GET.get('keyword', '')

    blogs = Blog.objects.filter(Q(title__icontains=keyword) | 
                                Q(short_description__icontains=keyword) |
                                Q (blog_body__icontains=keyword),
                                status="Published") 
    
    context = {
        'blogs':blogs,
        'keyword':keyword,
    }
    return render(request,'search.html', context)