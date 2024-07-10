from django.urls import path
from .views import AddTagView, AddAuthorView, AddQuoteView, HomeView, AuthorListView, AuthorDetailView, QuotesByTagView

app_name = 'app_quotes'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('author/<slug:slug>/', AuthorDetailView.as_view(), name='author_detail'),
    path('add_tag/', AddTagView.as_view(), name='add_tag'),
    path('add_author/', AddAuthorView.as_view(), name='add_author'),
    path('add_quote/', AddQuoteView.as_view(), name='add_quote'),
    path('tag/<str:tag>/', QuotesByTagView.as_view(), name='quotes_by_tag'),
]
