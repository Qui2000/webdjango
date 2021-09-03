from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic.base import TemplateView
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PostForm
from django.template.loader import render_to_string

# Create your views here.

class PostListView(ListView):
    queryset = Post.objects.all().order_by("date")
    template_name = 'blog/blog.html'
    context_object_name = 'Posts'
    paginate_by = 5

# def PostListView(request):
#     data = {'Posts' : Post.objects.all().order_by("-date")}
#     return render(request, 'blog/blog.html', data)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context

# def detailPost(request, id):
#     try:
#         post = Post.objects.get(id=id)
#     except Post.DoesNotExist:
#         raise Http404("Bài viết không tồn tại")
    
#     return render(request, 'blog/post.html', {'post': post})

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['title', 'body', 'image']
    success_url ="/blog/"

class PostChartView(TemplateView):
    template_name = 'blog/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.all()
        return context
    

class PostUpdateView(UpdateView):
    print("post edit here")
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body', 'image']
    success_url ="/blog/"

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url ="/blog/"

