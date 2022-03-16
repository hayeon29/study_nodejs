# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url'] #어떤 필드를 입력받을지
    success_url = reverse_lazy('list') #글쓰기 완료하고 이동할 페이지
    template_name_suffix = '_create' #모델명_XXX형태