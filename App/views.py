from django.shortcuts import render
from .models import Post
from django.views import generic


# Create your views here.
def home(request):

    post_list = Post.objects.filter(status=1).order_by('-created_on')

    context = {
        'post_list': post_list,
    }
    template_name='home.html'
    return render(request, template_name,context)
class PostList(generic.ListView):
    queryset=Post.objects.filter(status=1).order_by('-created_on')
   
    template_name='index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CATEGORY_CHOICES'] = Post.CATEGORY_CHOICES
        return context
class DetailView(generic.DetailView):

    model=Post
    template_name='post_detail.html'

    
