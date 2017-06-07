from django.db import models
from django.core.urlresolvers import reverse
from multiupload.fields import MultiFileField

class Brand(models.Model):
    name = models.CharField(max_length=250, unique=True)
    des = models.CharField(max_length=500)
    origin =  models.CharField(max_length=100)
    logo =  models.FileField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('watch:detail', kwargs={'pk': self.pk})



class Watch(models.Model):
    watch_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand")
    name =  models.CharField(max_length=50, verbose_name="Name")
    year =  models.CharField(max_length=10, verbose_name="Year")
    price = models.IntegerField()
    code = models.CharField(max_length=20, verbose_name="Code")
    ref_no = models.CharField(max_length=30, verbose_name="Ref. No.")
    type = models.CharField(max_length=50, verbose_name="Type", choices=(('all', 'All'),('men', "Men's"),('women', "Women's")))
    movement = models.CharField(max_length=50, verbose_name="Movement", choices=(('automatic', 'Automatic'),('manual', 'Manual'),('quartz', 'Quartz')))
    case_material = models.CharField(max_length=30, verbose_name="Case Material")
    color = models.CharField(max_length=30, verbose_name = "Color")
    bracelet_material = models.CharField(max_length=30, verbose_name="Bracelet Material")
    bracelet_color = models.CharField(max_length=30, verbose_name="Bracelet Color")
    bracelet_length = models.CharField(max_length=30, verbose_name="Bracelet Length")
    pic = models.ImageField()
    large_pic = models.FileField()
    featured = models.BooleanField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Carousel(models.Model):
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=1000)
    bg = models.FileField()