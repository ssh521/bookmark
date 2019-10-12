from django.urls import path

# view 에서 만들 클래스를 갖고 온다.
from .views import *
from .views import BookmarkListView, BookmarkCreateView, BookmarkUpdateView, BookmarkDeleteView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
]