from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from blogs.models import Blog, Comment, Category, FileUpload


def content(request):
    latest_blog_list = Blog.objects.all()
    context = {'latest_blog_list': latest_blog_list}
    return render(request, 'blogs/index.html', context)


def category(request, page_slug):
    get_category = Category.objects.get(page_slug=page_slug)
    latest_blog_list = Blog.objects.all().filter(category=get_category.id)
    context = {'latest_blog_list': latest_blog_list}
    return render(request, 'blogs/index.html', context)


def detail(request, page_slug):
    a_message = ""
    content = get_object_or_404(Blog, page_slug=page_slug)
    commentcollection = Comment.objects.all().filter(blog_id=content.pk)
    filecollection = FileUpload.objects.all().filter(blog_id=content.pk)

    if request.method == 'POST':
        commentcollection.create(user_id=request.POST['formuser'], comment=request.POST['comments'], blog_id=content.pk)
        a_message = "Comment is added"
    return render(request, 'blogs/detail.html', {
        'content': content,
        'a_message': a_message,
        'commentcollection': commentcollection,
        'filecollection':filecollection,
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(request.POST['next'])
    else:
        form = UserCreationForm()
    nextpage = request.GET.get('next')
    return render(request, "registration/register.html", {
        'form': form,
        'nextpage': nextpage,
    })
