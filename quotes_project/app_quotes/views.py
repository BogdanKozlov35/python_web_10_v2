from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .forms import TagForm, AuthorForm, QuoteForm
from .models import Quote, Authors, Tag


class HomeView(ListView):
    model = Quote
    template_name = 'app_quotes/home.html'
    context_object_name = 'quotes'
    paginate_by = 10  # Кількість цитат на сторінку

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quotes_list = self.get_queryset()
        paginator = Paginator(quotes_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            quotes = paginator.page(page)
        except PageNotAnInteger:
            quotes = paginator.page(1)
        except EmptyPage:
            quotes = paginator.page(paginator.num_pages)

        context['quotes'] = quotes
        context['top_tags'] = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]
        return context


class AuthorListView(ListView):
    model = Authors
    template_name = 'app_quotes/author_detail.html'
    context_object_name = 'authors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        context['quotes'] = Quote.objects.filter(author=author)
        return context


class AuthorDetailView(DetailView):
    model = Authors
    template_name = 'app_quotes/author_detail.html'
    context_object_name = 'author'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        quotes_list = Quote.objects.filter(author=author)
        paginator = Paginator(quotes_list, 10)  # Add pagination
        page = self.request.GET.get('page')

        try:
            quotes = paginator.page(page)
        except PageNotAnInteger:
            quotes = paginator.page(1)
        except EmptyPage:
            quotes = paginator.page(paginator.num_pages)

        context['quotes'] = quotes
        return context


class AddTagView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Tag
    template_name = "app_quotes/add_tag.html"
    success_url = reverse_lazy('app_quotes:home')
    form_class = TagForm


class AddAuthorView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Authors
    template_name = "app_quotes/add_author.html"
    success_url = reverse_lazy('app_quotes:home')
    form_class = AuthorForm


class AddQuoteView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Authors
    template_name = "app_quotes/add_quote.html"
    success_url = reverse_lazy('app_quotes:home')
    form_class = QuoteForm


def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'app_quotes/home.html', {'quotes': quotes})


class QuotesByTagView(ListView):
    model = Quote
    template_name = 'app_quotes/quotes_by_tag.html'
    context_object_name = 'quotes'

    def get_queryset(self):
        tag = get_object_or_404(Tag, name=self.kwargs['tag'])
        return Quote.objects.filter(tags=tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag']
        return context
