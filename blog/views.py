from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTopicForm
from .models import Blog, Topic, Post

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

def blog_topics(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'topics.html', {'blog': blog})


def new_topic(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save()
            return redirect('blog_topics', pk=blog.pk)
    else:
         form = NewTopicForm()
    return render(request, 'new_topic.html', {'blog':blog,'form': form})