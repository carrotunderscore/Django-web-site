import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from .models import BlogPost


def blog_view(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None

    blogPosts = BlogPost.objects.all()
    blogList = []
    for row in blogPosts:
        blogObject = {"title": row.title, "content": row.content, "published_date": row.pub_date}
        blogList.append(blogObject)

    context = {'username': None, "blogList": blogList}

    return render(request, 'blog_view.html', context)


def blog_admin_view():
    return None


def create_post_view(request):
    return render(request, 'create_post_view.html')


def publish_post(request):
    if request.method == 'POST':
        user = User.objects.get(pk=16)
        data = json.load(request)
        blogObject = data.get('blogObject')
        title = blogObject['title']
        content = blogObject['content']

        newBlogPost = BlogPost(
            title=title,
            content=content,
            author=user)
        newBlogPost.save()
        return render(request, 'blog_admin_view.html')
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)