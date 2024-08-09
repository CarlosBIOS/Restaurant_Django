from django.shortcuts import render, redirect
from django.views import generic
from .models import Item, MEAL_TYPE, STATUS


class MenuList(generic.ListView):
    queryset = Item.objects.order_by('-date_created')
    template_name = 'index.html'

    # Com esta função, já incluída no generic.ListView, context vai-se tornar uma variável no ficheiro index.html!!
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meals'] = MEAL_TYPE
        return context


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = 'menu_item_detail.html'
