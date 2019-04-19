from cats.models import Cat, Comment

from django.views import View
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from cats.forms import CommentForm
from cats.util import CatsListView, CatsDetailView, CatsCreateView, CatsUpdateView, CatsDeleteView

class CatListView(CatsListView):
    model = Cat
    template_name = "cats/cat_list.html"

class CatDetailView(CatsDetailView):
    model = Cat
    template_name = "cats/cat_detail.html"
    def get(self, request, pk) :
        cat = Cat.objects.get(id=pk)
        comments = Comment.objects.filter(cat=cat).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'cat' : cat, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)


class CatCreateView(CatsCreateView):
    model = Cat
    fields = ['name', 'foods', 'weight']
    template_name = "cats/cat_form.html"

class CatUpdateView(CatsUpdateView):
    model = Cat
    fields = ['name', 'foods', 'weight']
    template_name = "cats/cat_form.html"

class CatDeleteView(CatsDeleteView):
    model = Cat
    template_name = "cats/cat_delete.html"

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Cat, id=pk)
        comment_form = CommentForm(request.POST)

        comment = Comment(text=request.POST['comment'], owner=request.user, cat=f)
        comment.save()
        return redirect(reverse_lazy('cat_detail', args=[pk]))

class CommentDeleteView(CatsDeleteView):
    model = Comment
    template_name = "cats/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        cat = self.object.cat
        return reverse_lazy('cat_detail', args=[cat.id])