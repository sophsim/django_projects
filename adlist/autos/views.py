from autos.models import Auto, Comment

from django.views import View
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from autos.forms import CommentForm
from autos.util import AutosListView, AutosDetailView, AutosCreateView, AutosUpdateView, AutosDeleteView

class AutoListView(AutosListView):
    model = Auto
    template_name = "auto_list.html"

class AutoDetailView(AutosDetailView):
    model = Auto
    template_name = "auto_detail.html"
    def get(self, request, pk) :
        auto = Auto.objects.get(id=pk)
        comments = Comment.objects.filter(auto=auto).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'auto' : auto, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)


class AutoCreateView(AutosCreateView):
    model = Auto
    fields = ['name', 'detail', 'mileage']
    template_name = "auto_form.html"

class AutoUpdateView(AutosUpdateView):
    model = Auto
    fields = ['name', 'detail', 'mileage']
    template_name = "auto_form.html"

class AutoDeleteView(AutosDeleteView):
    model = Auto
    template_name = "auto_delete.html"

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Auto, id=pk)
        comment_form = CommentForm(request.POST)

        comment = Comment(text=request.POST['comment'], owner=request.user, auto=f)
        comment.save()
        return redirect(reverse_lazy('auto_detail', args=[pk]))

class CommentDeleteView(AutosDeleteView):
    model = Comment
    template_name = "comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        auto = self.object.auto
        return reverse_lazy('auto_detail', args=[auto.id])