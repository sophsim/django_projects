from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from stars.models import Star, Type
from stars.forms import MakeForm

# Create your views here.

class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        mc = Type.objects.all().count();
        al = Star.objects.all();

        ctx = { 'make_count': mc, 'star_list': al };
        return render(request, 'stars/star_list.html', ctx)

class TypeView(LoginRequiredMixin,View) :
    def get(self, request):
        ml = Type.objects.all();
        ctx = { 'type_list': ml };
        return render(request, 'stars/type_list.html', ctx)

class TypeCreate(LoginRequiredMixin, View):
    template = 'stars/type_form.html'
    success_url = reverse_lazy('stars')
    def get(self, request) :
        form = MakeForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = MakeForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        make = form.save()
        return redirect(self.success_url)

class TypeUpdate(LoginRequiredMixin, View):
    model = Type
    success_url = reverse_lazy('stars')
    template = 'stars/type_form.html'
    def get(self, request, pk) :
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance = make)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class TypeDelete(LoginRequiredMixin, DeleteView):
    model = Type
    success_url = reverse_lazy('stars')
    template = 'stars/type_confirm_delete.html'

    def get(self, request, pk) :
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        ctx = { 'make': make }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)

# Take the easy way out on the main table
class StarCreate(LoginRequiredMixin,CreateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars')

class StarUpdate(LoginRequiredMixin, UpdateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars')

class StarDelete(LoginRequiredMixin, DeleteView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars')