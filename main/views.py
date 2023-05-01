from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')


# from django.urls import reverse_lazy
# from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# from .models import MenuItem, Category
# from .forms import MenuItemForm

# class IndexView(TemplateView):
#     template_name = 'main/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu_items'] = MenuItem.objects.all()
#         context['categories'] = Category.objects.all()
#         return context


# class MenuItemListView(ListView):
#     model = MenuItem
#     template_name = 'main/menu_item_list.html'
