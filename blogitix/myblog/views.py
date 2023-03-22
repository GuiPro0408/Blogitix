from django.shortcuts import render
from django.views import generic
from .models import Post, Category
from .forms import PostForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm # This line adds the form to the view.
    template_name = 'add_post.html'
    
    # get_initial is a special method that is used to set the initial values for the fields in the form.
    def get_initial(self):
        # Here we call the get_initial method from the parent class to
        initial = super().get_initial() 
        # Then we override the default values for the fields in the form.
        initial['category'] = Category.objects.order_by('pk').first() or Category.objects.create(name='Uncategorized')
        initial['author'] = self.request.user
        return initial

class UpdatePostView(generic.UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['content']
