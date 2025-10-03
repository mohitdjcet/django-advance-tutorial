from django.shortcuts import render
from .models import Post
from django.db.models import Q

def post_list(request):
    query = request.GET.get('q') # serach keyword
    category = request.GET.get('category') # category filter

    posts = Post.objects.all()

    #Search using Q objects
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) 
        )

    # Filter by category
    if category:
        posts = posts.filter(catagory__iexact=category)

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'query': query,
        'category': category,
    })

