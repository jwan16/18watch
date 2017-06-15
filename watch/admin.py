from django.contrib import admin
from .models import Brand, Watch, Carousel, watch_category

admin.site.register(Brand)
admin.site.register(Watch)
admin.site.register(Carousel)
admin.site.register(watch_category)