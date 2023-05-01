from django.urls import path
from . import views
from .views import IndexView, MenuItemListView, MenuItemDetailView, MenuItemCreateView, MenuItemUpdateView, MenuItemDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('menu', MenuItemListView.as_view(), name='menu_item_list'),
    path('<slug:slug>/', MenuItemDetailView.as_view(), name='menu_item_detail'),
    path('create/', MenuItemCreateView.as_view(), name='menu_item_create'),
    path('update/<slug:slug>/', MenuItemUpdateView.as_view(), name='menu_item_update'),
    path('delete/<slug:slug>/', MenuItemDeleteView.as_view(), name='menu_item_delete'),
]