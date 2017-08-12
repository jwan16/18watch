from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .models import Brand, Watch, Carousel
from django.shortcuts import render_to_response
from django.db.models import Q
import operator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from numbers import Number
from functools import reduce
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin


def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('index.html',{'state':state, 'username': username})

# class IndexView(generic.ListView):
#     template_name = 'watch/index.html'
#     context_object_name = 'all_brands'
#
#     def get_queryset(self):
#         return Brand.objects.all()

def IndexView(request):
    brand_list = Brand.objects.all()
    watch_list = Watch.objects.all()
    carousel_list = Carousel.objects.all()
    feature_list = watch_list.filter(featured=True)
    latest_list = watch_list.order_by('pub_date')[:4]
    context = {
        "watch_list": watch_list,
        "brand_list": brand_list,
        "feature_list": feature_list,
        "latest_list": latest_list,
        "carousel_list": carousel_list,
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
    print(filter_brand)
    if filter_price_max:
        request.session['filter_price_max'] = filter_price_max
    if filter_price_min:
        request.session['filter_price_min'] = filter_price_min
    if len(filter_color) >= 0:
        request.session['filter_color'] = filter_color
    if len(filter_brand) >= 0:
        request.session['filter_brand'] = filter_brand
    print(request.session.get('filter_color'))

    # Filter Max/Min Price
    if request.session['filter_price_max'] is not None:
        filtered_list = filtered_list.filter(price__lt=request.session.get('filter_price_max'))
    if request.session['filter_price_min'] is not None:
        filtered_list = filtered_list.filter(price__gt=request.session.get('filter_price_min'))

    # Filter brand, color, movement,
    if request.session.get('filter_color') is not None:
        if len(request.session.get('filter_color')) > 0:
            filtered_list = filtered_list.filter(color__in=request.session.get('filter_color'))
    print(request.session.get('filter_brand'))
    if request.session.get('filter_brand') is not None:
        if len(request.session.get('filter_brand')) > 0:
            filtered_list = filtered_list.filter(watch_brand__name__in=request.session.get('filter_brand'))

    # filter_brand_list = request.POST.getlist("selected_brand[]")
    # if filter_brand_list:
    #     filtered_list = filtered_list.filter(watch_brand__name__in=filter_brand_list)
    # filter_color_list = request.POST.getlist("selected_color[]")
    # if filter_color_list:
    #     filtered_list = filtered_list.filter(watch_color__name__in=filter_color_list)

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

