from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import CreateView, ListView, DetailView
from .models import Articles, Comments
from .forms import CommentForm
# Create your views here.
#######################################################################
#Article
#######################################################################
class ArticlesListView(ListView):
    model = Articles
    def get_queryset(self):
        return Articles.objects.order_by('-date')

class ArticlesDetail(DetailView):
    model = Articles

#######################################################################
#Comments
#######################################################################
def add_comment(request, pk):
    article = get_object_or_404(Articles, pk = pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.article = article
            comment.save()
            return redirect('blog:article_detail', pk = pk)
    else:
        form = CommentForm()
        return render(request, 'blog/comment_form.html', {'form' : form})
