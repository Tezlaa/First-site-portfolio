from django.shortcuts import render, get_object_or_404
from .models import My_blog

# Create your views here.
def all_blogs(request):
    my_blog = My_blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'my_blog':my_blog}, )

def detail(request, blog_id):
    blog = get_object_or_404(My_blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})