from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post


def index(request):
    posts = Post.objects.all()
    print(posts)

    return render(request, 'blog/index.html', context={
        'posts': posts
    })
    # return HttpResponse("欢迎访问我的博客首页")


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/detail.html', context={'post': post})


"""
@app.route('/')
def index():
    return 'xxxx'
    return  render_template('xxxx.html', name=name, welcome=welcome)
    
@app.route('/post/<id>'/) 
def detail(id):
    return id   
    

"""
