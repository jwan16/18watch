# -*- coding: utf-8 -*-

from django.views import generic
from django.shortcuts import render, redirect
from .models import Brand, Watch, Carousel
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotAllowed

def IndexView(request):
    brand_list = Brand.objects.all()
    browse_by_brand_list = Brand.objects.all()[:4]

    watch_list = Watch.objects.all()
    carousel_list = Carousel.objects.all()
    feature_list = watch_list.filter(featured=True)
    latest_list = watch_list.order_by('pub_date')[:4]
    movement_list = Watch.objects.values_list('movement', flat=True).distinct()
    request.session.setdefault('filter_price_max', 100000)
    request.session.setdefault('filter_price_min', 0)
    context = {
        "watch_list": watch_list,
        "browse_by_brand_list": browse_by_brand_list,
        "brand_list": brand_list,
        "feature_list": feature_list,
        "latest_list": latest_list,
        "carousel_list": carousel_list,
        "movement_list": movement_list,
    }
    return render(request, "watch/index.html", context)


def WatchList(request):
    brand_list = Brand.objects.all()
    watch_list = Watch.objects.all()
    color_list = Watch.objects.values_list('color', flat=True).distinct()
    movement_list = Watch.objects.values_list('movement', flat=True).distinct()
    no_of_available = Watch.objects.all().count
    query = request.GET.get("q")
    filter = request.GET.get("filter")
    category_query = request.GET.get("query")
    if query:
        watch_list = watch_list.filter(
            Q(name__icontains=query)|
            Q(year__icontains=query)
            ).distinct()
    if filter:
        watch_list = watch_list.filter

    # Paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(watch_list, 12)
    try:
        watch_list = paginator.page(page)
    except PageNotAnInteger:
        watch_list = paginator.page(1)
    except EmptyPage:
        watch_list = paginator.page(paginator.num_pages)

    selected_brand_list = request.session.get('filter_brand')
    selected_movement_list = request.session.get('filter_movement')

    print(selected_movement_list)
    request.session.setdefault('filter_price_max', 100000)
    request.session.setdefault('filter_price_min', 0)
    filter_price_max = request.session.get('filter_price_max')
    filter_price_min = request.session.get('filter_price_min')

    context = {
        "watch_list": watch_list,
        "brand_list": brand_list,
        "color_list": color_list,
        "movement_list": movement_list,
        "List": "List",
        "no_of_available": no_of_available,
        "filter_price_max": filter_price_max,
        "filter_price_min": filter_price_min,
        "selected_brand_list": selected_brand_list,
        "selected_movement_list": selected_movement_list,
    }

    return render(request, "watch/product.html",context)

# def search_name(request):
#     if request.method == "POST":
#         search_text = request.POST['search_text']
#     else:
#         search_text = ''
#
#     watch_list = Watch.objects.filter(name__icontains=search_text)
#
#     context = {
#         "watch_list": watch_list,
#     }
#     return render(request, "watch/search_result.html",context)
#
# class detail_list(generic.DetailView):
#     model = Watch
#     template_name = 'watch/product_detail.html'



def filter(request):
    brand_list = Brand.objects.all()
    filtered_list = Watch.objects.all()

    # Filter Max Price



    # Get Ajax
    filter_price_max = request.POST.get("filter_price_max")
    filter_price_min = request.POST.get("filter_price_min")
    filter_color = request.POST.getlist("selected_color[]")
    filter_brand = request.POST.getlist("selected_brand[]")
    filter_movement = request.POST.getlist("selected_movement[]")
    print(filter_brand)
    if filter_price_max:
        request.session['filter_price_max'] = filter_price_max
    if filter_price_min:
        request.session['filter_price_min'] = filter_price_min
    if len(filter_color) >= 0:
        request.session['filter_color'] = filter_color
    if len(filter_brand) >= 0:
        request.session['filter_brand'] = filter_brand
    if len(filter_movement) >= 0:
        request.session['filter_movement'] = filter_movement
    # Filter Max/Min Price
    if request.session['filter_price_max'] is not None:
        filtered_list = filtered_list.filter(price__lt=request.session.get('filter_price_max'))
    if request.session['filter_price_min'] is not None:
        filtered_list = filtered_list.filter(price__gt=request.session.get('filter_price_min'))

    # Filter brand, color, movement,
    if request.session.get('filter_color') is not None:
        if len(request.session.get('filter_color')) > 0:
            filtered_list = filtered_list.filter(color__in=request.session.get('filter_color'))
    if request.session.get('filter_brand') is not None:
        if len(request.session.get('filter_brand')) > 0:
            filtered_list = filtered_list.filter(watch_brand__name__in=request.session.get('filter_brand'))
    if request.session.get('filter_movement') is not None:
        if len(request.session.get('filter_movement')) > 0:
            filtered_list = filtered_list.filter(movement__in=request.session.get('filter_movement'))

    # Filter top search bar
    search_query = request.session.get('search_query')
    if search_query:
        filtered_list = filtered_list.filter(
            Q(name__icontains=search_query)|
            Q(year__icontains=search_query)|
            Q(watch_brand__name__icontains=search_query)|
            Q(color__icontains=search_query)|
            Q(movement__icontains=search_query)
            ).distinct()


    context = {
        "filtered_list": filtered_list,
        # 'selected_brand': selected_brand,
    }
    return render(request, "watch/search_result.html",context)

class DetailList(generic.DetailView):
    model = Watch
    template_name = 'watch/product_detail.html'

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())




class InventoryByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = Watch
    context_object_name = 'watches'
    template_name = 'watch/inventory.html'
    paginate_by = 10

    def get_queryset(self):
        return Watch.objects.filter(owner=self.request.user)

def update_session(request):
    if not request.is_ajax() or not request.method=='POST':
        return HttpResponseNotAllowed(['POST'])
    print('update_session is working.')
    filter_price_max = request.POST.get("filter_price_max")
    filter_price_min = request.POST.get("filter_price_min")
    filter_brand = request.POST.getlist("selected_brand[]")
    filter_movement = request.POST.getlist("selected_movement[]")
    search_query = request.POST.get('custom-search-input')
    if search_query is not None:
        request.session['search_query'] = search_query
    if filter_price_max:
        request.session['filter_price_max'] = filter_price_max
    if filter_price_min:
        request.session['filter_price_min'] = filter_price_min
    if len(filter_brand) >= 0:
        request.session['filter_brand'] = filter_brand
    if len(filter_movement) >= 0:
        request.session['filter_movement'] = filter_movement
    print(request.session.get('search_query'))
    return HttpResponse('ok')