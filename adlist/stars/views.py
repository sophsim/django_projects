from stars.models import Star, Comment

from django.views import View
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from stars.forms import CommentForm
from stars.util import StarsListView, StarsDetailView, StarsCreateView, StarsUpdateView, StarsDeleteView

class StarListView(StarsListView):
    model = Star
    template_name = "stars/star_list.html"

class StarDetailView(StarsDetailView):
    model = Star
    template_name = "stars/star_detail.html"
    def get(self, request, pk) :
        star = Star.objects.get(id=pk)
        comments = Comment.objects.filter(star=star).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'star' : star, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)


class StarCreateView(StarsCreateView):
    model = Star
    fields = ['name', 'distance', 'diameter']
    template_name = "stars/star_form.html"

class StarUpdateView(StarsUpdateView):
    model = Star
    fields = ['name', 'distance', 'diameter']
    template_name = "stars/star_form.html"

class StarDeleteView(StarsDeleteView):
    model = Star
    template_name = "stars/star_delete.html"

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Star, id=pk)
        comment_form = CommentForm(request.POST)

        comment = Comment(text=request.POST['comment'], owner=request.user, star=f)
        comment.save()
        return redirect(reverse_lazy('star_detail', args=[pk]))

class CommentDeleteView(StarsDeleteView):
    model = Comment
    template_name = "stars/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        star = self.object.star
        return reverse_lazy('star_detail', args=[star.id])