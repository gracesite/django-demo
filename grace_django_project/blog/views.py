from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# hard coded data
# allposts = [
#     {
#         'author': 'Grace T',
#         'title': 'Blog Post 1',
#         'content': 'First post of the Blog',
#         'date_posted': 'July 18, 2022'
#     },
#     {
#         'author': 'Ava W',
#         'title': 'Blog Post 2',
#         'content': '2nd post of the Blog',
#         'date_posted': 'July 19, 2022'
#     },
# ]
def home(request):
    context = {
        'posts': Post.objects.all(),  # <--- data are from Database Models
    }
    return render(request, 'blog/home.html', context) # homePage has no Title

def about(request):
    return render(request, 'blog/about.html', {'title':'AboutTitle'}) # AboutTitle
# Create your views here.
