from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import MenuItem, Category
from .forms import MenuItemForm

class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = MenuItem.objects.all()
        context['categories'] = Category.objects.all()
        return context


class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'main/menu_item_list.html'


class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = 'main/menu_item_detail.html'
    slug_url_kwarg = 'slug'


class MenuItemCreateView(CreateView):
    model = MenuItem
    template_name = 'main/menu_item_create.html'
    form_class = MenuItemForm
    success_url = reverse_lazy('menu_item_list')


class MenuItemUpdateView(UpdateView):
    model = MenuItem
    template_name = 'main/menu_item_update.html'
    form_class = MenuItemForm
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('menu_item_list')


class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = 'main/menu_item_delete.html'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('menu_items:list')
