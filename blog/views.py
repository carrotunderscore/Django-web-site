import json
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import NewPostForm, EditPostForm


def blog_view(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None

    blogPosts = BlogPost.objects.all()
    blogList = []
    for row in blogPosts:
        blogObject = {"title": row.title, "content": row.content, "published_date": row.pub_date, "blogPostId": row.id}
        blogList.append(blogObject)

    context = {'username': None, "blogList": blogList}

    return render(request, 'blog_view.html', context)


def blog_admin_view():
    return None


def create_post_view(request):
    return render(request, 'create_post_view.html')


def publish_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            user = User.objects.get(pk=16)
            newBlogPost = BlogPost(
                title=title,
                content=content,
                author=user)
            newBlogPost.save()
        return render(request, 'blog_view.html')
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


def delete_post(request):
    if request.method == 'POST':
        data = json.load(request)
        blogObject = data.get('blogObject')
        blogPostId = blogObject['blogPostId']

        post = BlogPost.objects.get(id=blogPostId)
        post.delete()


def edit_post_view(request, pk):
    post = BlogPost.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/blog/')
    else:
        form = EditPostForm(instance=post)

    context = {'form': form, 'post': post}
    return render(request, 'edit_post.html', context)

