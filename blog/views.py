import json
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import BlogPost
from .models import Projects
from .forms import NewPostForm, EditPostForm, EditProjectForm


def blog_post_view(request, pk):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    blogList = []
    post = BlogPost.objects.get(pk=pk)
    blogObject = {"title": post.title, "content": post.content, "published_date": post.pub_date, "blogPostId": post.id}

    context = {'username': None, "blogList": blogObject}

    return render(request, 'blogPosts/blog_view.html', context)


def create_post_view(request):
    return render(request, 'createPosts/create_post_view.html')


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
            return redirect('/post/' + str(pk))
    else:
        form = EditPostForm(instance=post)

    context = {'form': form, 'post': post}
    return render(request, 'editPosts/edit_post.html', context)


def blog_posts_list_view(request):
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

    return render(request, 'blogPosts/blog_posts_list_view.html', context)


def projects_list_view(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None

    projects = Projects.objects.all()
    projectsList = []
    for row in projects:
        projectObject = {
            "title": row.title,
            "content": row.content,
            "published_date": row.pub_date,
            "blogPostId": row.id,
            "imageUrl": row.image_url,
            "githubUrl": row.github_url
        }
        projectsList.append(projectObject)

    context = {'username': None, "projectList": projectsList}

    return render(request, 'projects/projects_list_view.html', context)


def create_project_view(request):
    return render(request, 'createPosts/create_project_view.html')


def publish_project(request):
    if request.method == 'POST':
        raw_data = request.body.decode('utf-8')
        data = json.loads(raw_data)
        title = data.get('title')
        imageUrl = data.get('imageUrl')
        githubUrl = data.get('githubUrl')
        content = data.get('content')
        user = User.objects.get(pk=16)
        newProject = Projects(
            title=title,
            image_url=imageUrl,
            github_url=githubUrl,
            content=content,
            author=user)
        newProject.save()

        return render(request, 'projects/projects_list_view.html')
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


def project_view(request, pk):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    post = Projects.objects.get(pk=pk)
    projectObject = {
        "title": post.title,
        "content": post.content,
        "published_date": post.pub_date,
        "projectId": post.id,
        "imageUrl": post.image_url,
        "githubUrl": post.github_url
    }
    context = {'username': None, "project": projectObject}
    return render(request, 'projects/project_view.html', context)


def delete_project(request):
    if request.method == 'POST':
        data = json.load(request)
        projectObject = data.get('projectObject')
        projectId = projectObject['projectId']

        post = Projects.objects.get(id=projectId)
        post.delete()


def edit_project_view(request, pk):
    project = Projects.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/project/' + str(pk))
    else:
        form = EditProjectForm(instance=project)

    context = {'form': form, 'post': project}
    return render(request, 'editPosts/edit_project.html', context)


def about_me_view(request):
    return render(request, 'about_me_view.html')

