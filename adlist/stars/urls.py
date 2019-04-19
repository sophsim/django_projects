from django.urls import path, reverse_lazy
from . import views


urlpatterns = [
    path('', views.StarListView.as_view(), name='stars'),
    path('stars', views.StarListView.as_view(), name='stars'),
    path('star/<int:pk>', views.StarDetailView.as_view(), name='star_detail'),
    path('star/create',
        views.StarCreateView.as_view(success_url=reverse_lazy('stars')), name='star_create'),
    path('star/<int:pk>/update',
        views.StarUpdateView.as_view(success_url=reverse_lazy('stars')), name='star_update'),
    path('star/<int:pk>/delete',
        views.StarDeleteView.as_view(success_url=reverse_lazy('stars')), name='star_delete'),
    path('star/<int:pk>/comment',
        views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('stars')), name='comment_delete'),
]