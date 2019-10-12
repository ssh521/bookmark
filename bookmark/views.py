from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


from django.urls import reverse_lazy

from .models import Bookmark

# 리스트 클래스
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 4

    # 템플릿 페이지 접미사 지정하기. 앱이름_listview
    template_name_suffix = '_list'

# 입력 클래스..
class BookmarkCreateView(CreateView):

    # 데이타 테이블
    model = Bookmark

    # 보여줄 필드
    fields = ['site_name', 'url']

    # 성공시 이동할 페이지
    success_url = reverse_lazy('list')

    # 템플릿 페이지 접미사 지정하기.
    template_name_suffix = '_create'

# 자세히보기 클래스
class BookmarkDetailView(DetailView):
    model = Bookmark

    # 템플릿 페이지 접미사 지정하기.
    template_name_suffix = '_detail'

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    #success_url = reverse_lazy('list')

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
