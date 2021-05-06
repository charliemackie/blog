from django.shortcuts import render, redirect
from django.db.models import F
from django.http import HttpResponse

from .models import Post

# Create your views here.

def home(request):
    stories = Post.objects.all()
    context = {
        'stories': stories,
        'activity': False
    }
    return render(request, 'posts/home.html', context)

def filter_category(request, category=None):

    # logic for filtering posts

    if (category == 'Engineering'):
        stories = Post.objects.filter(category='Engineering')
    elif (category == 'Data'):
        stories = Post.objects.filter(category='Data')
    elif (category == 'Business'):
        stories = Post.objects.filter(category='Business')
    else:
        stories = Post.objects.all()

    context = {
        'stories': stories,
        'activity': True
    }

    return render(request, 'posts/home.html', context)

def story_like(request, story_id=None, story_name=None):
	if request.method == "POST":
		Post.objects.filter(pk=story_id).update(likes=F('likes') + 1)
		# Return success code
		return HttpResponse(200)
	return HttpResponse(400)

def The_Data_Supply_Chain(request):

    stories = Post.objects.filter(name='The Data Supply Chain')

    context = {
        'stories': stories
    }
    
    return render(request, 'posts/The_Data_Supply_Chain.html', context)



