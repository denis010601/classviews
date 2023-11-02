from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import *
from .forms import ArticleForm, CustomUserCreationForm

class HomeView(TemplateView):
    template_name = 'classviewshome/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_date'] = 'Доп информация'
        return context

class ArticleListView(ListView):
    model = Article
    print(Article)
    # template_name = 'articles.html'
    # context_object_name = 'articles'
class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_books'] = Book.objects.filter(article=self.object)
        return context


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = '/articles/'





class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm

    template_name = 'classviewshome/register.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        user = form.save(commit=False)
        user.full_name =form.cleaned_data['full_name']
        user.birth_date = form.cleaned_data['birth_date']
        user.save()
        login(self.request, user)
        return super().form_valid(form)



# class BookListView(ListView):
#     model = Book

# def articleDetail(request, pk):
#     article = Article.object.get(pk=pk)
#     return render(request, 'classviewshome/article_detail.html' , context={'article': article})