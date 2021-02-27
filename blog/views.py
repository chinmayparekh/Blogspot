from django.shortcuts import render
from .models import Post
#dummy data
posts = [
    {
        'author':'Chinmay Parekh',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'Feb 20, 2021'
    },
    {
        'author': 'ABCD',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Feb 19, 2021'
    }
]

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})
